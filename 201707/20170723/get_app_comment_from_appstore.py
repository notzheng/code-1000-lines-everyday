# -----------------------------------------------------------------------------------------------------------------------
# at first, you must install package request and xlsx writer
# for windows,
# 1.press windows key + R , open the 'run' Dialog box
# 2.input 'cmd' to open the  command
# 3.input 'pip install packageName' then press Enter Key (packageName is name of the package you want to install)
# if it doesn't work, please search the solution on Goole or other search engine
# -----------------------------------------------------------------------------------------------------------------------

import requests, xlsxwriter

# -----------------------------------------------------------------
# this function is to get app info (app name,description etc....)
# return a dict including app_info
# one argument: 'app_id'
# -----------------------------------------------------------------
def get_app_info(app_id):
    app_info_url = "https://itunes.apple.com/lookup?cc=cn&id=" + str(app_id)
    print('Getting app info...')
    app_info_data = requests.get(app_info_url)
    app_info_json = app_info_data.json()['results'][0]    #return data format to json, then put some key to dict
    app_info = {
        'appName': app_info_json['trackName'],
        'description': app_info_json['description'],
        'releaseDate': app_info_json['releaseDate'],
        'currentVersionReleaseDate': app_info_json['currentVersionReleaseDate']
    }
    print('Getting app ' + app_info['appName'] + ' info Done!')
    return app_info

# ---------------------------------------------------------------------------------------------------------------------
# this function is to get app rate info (rate count, average rate, 1 star to 5 star count, etc....) and comment count
# return a dict including app_info
# one argument: 'app_id'
# ----------------------------------------------------------------------------------------------------------------------
def get_app_rate_reviewnum(app_id):
    app_rr_url = 'https://itunes.apple.com/cn/customer-reviews/id' + str(app_id) + '?dataOnly=true&displayable-kind=11'
    app_rr_header = {
        'user-agent': 'iTunes/12.6.1 (Macintosh; OS X 10.12.5) AppleWebKit/603.2.4'
    }
    print('Getting app rate...')
    app_rr_data = requests.get(app_rr_url, headers=app_rr_header)
    app_rr_json = app_rr_data.json()  # seem like function get_app_info()
    if 'ratingCount' in app_rr_json.keys():
        app_rr_info = {
            'reviewsNum': app_rr_json['totalNumberOfReviews'],
            'rateCount': app_rr_json['ratingCount'],
            'rateList': app_rr_json['ratingCountList'],
            'rateAvg': app_rr_json['ratingAverage']
        }
    else:
        app_rr_info = {
            'reviewsNum': app_rr_json['totalNumberOfReviews'],
            'rateCount': 'none',
            'rateList': 'none',
            'rateAvg': 'none'
        }
    print('Getting app rate Done!')
    return app_rr_info

# -------------------------------------------------------------------------------------------------------------
# this function is to get All app comment  return a
# return All comment
# two argument: 'app_id' 'reviewsNum'(means comment count, refer the data funtion get_app_rate_info() return)
# --------------------------------------------------------------------------------------------------------------
def get_app_review_all(app_id, reviewsNum):
    def get_app_review(app_id, start_index, end_index):
        app_review_url = 'https://itunes.apple.com/WebObjects/MZStore.woa/wa/userReviewsRow'
        app_review_query_str = {
            'cc': 'cn',
            'id': app_id,
            'displayable-kind': '11',
            'startIndex': start_index,
            'endIndex': end_index,
            'sort': '4',
            'appVersion': 'all'
        }
        app_review_headers = {
            'user-agent': 'iTunes/12.6.1 (Macintosh; OS X 10.12.5) AppleWebKit/603.2.4',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }
        app_review_data = requests.get(app_review_url, app_review_query_str, headers=app_review_headers)
        app_review = app_review_data.json()['userReviewList']
        return app_review
    # to avoid request error, we get only 5000 comment every time
    if reviewsNum < 5000:
        print('Getting 0 - %d app review...' % reviewsNum)
        app_review_all = get_app_review(app_id, 0, reviewsNum)
        print('Done!')
        return app_review_all
    else:
        reviews_num_list = list(range(0, reviewsNum, 5000))
        reviews_num_list.append(reviewsNum)
        app_review_all = []
        for a in range(0, len(reviews_num_list) - 1):
            print('Getting ' + str(reviews_num_list[a]+1) + ' - ' + str(reviews_num_list[a + 1]) + ' app review...')
            single_review = get_app_review(app_id, reviews_num_list[a], reviews_num_list[a + 1])
            print('Done!')
            app_review_all += single_review
        return app_review_all

# --------------------------------------------------------------------------------------------------
# this function is to write All app comment  and app rate info to excel
# three argument:
# 1.'app_info' (get app name for excel .xlsx's name, refer the data funtion get_app_info() return)
# 2.'app_rr_info' (get app rate info, refer the data funtion get_app_rate_info() return)
# 3.'app_review_all' (get All app comment, refer the data funtion get_app_rate_info() return)
# --------------------------------------------------------------------------------------------------
def app_info_to_excel(app_info, app_rr_info, app_review_all):
    print('Writing to Excel...')
    workbook = xlsxwriter.Workbook(str(app_info['appName']) + '(' + str(app_rr_info['reviewsNum']) + '条).xlsx')
    worksheet1 = workbook.add_worksheet('评论')
    title = ['评论id', '标题', '评论内容', '评论时间', '评分', '有帮助次数', '被评价总数', '评价者昵称', '是否编辑', '评论者类型']
    worksheet1.write_row('A1', title)
    row = 1
    col = 0
    for comm in app_review_all:
        worksheet1.write(row, col, comm['userReviewId'])
        worksheet1.write(row, col + 1, comm['title'])
        worksheet1.write(row, col + 2, comm['body'])
        worksheet1.write(row, col + 3, comm['date'])
        worksheet1.write(row, col + 4, comm['rating'])
        worksheet1.write(row, col + 5, comm['voteSum'])
        worksheet1.write(row, col + 6, comm['voteCount'])
        worksheet1.write(row, col + 7, comm['name'])
        worksheet1.write(row, col + 8, comm['isEdited'])
        worksheet1.write(row, col + 9, comm['customerType'])
        row += 1

    worksheet2 = workbook.add_worksheet('信息与评分')
    worksheet2.write(0, 0, 'App名称')
    worksheet2.write(0, 1, app_info['appName'])
    worksheet2.write(1, 0, 'App描述')
    worksheet2.write(1, 1, app_info['description'])
    worksheet2.write(2, 0, 'App上架日期')
    worksheet2.write(2, 1, app_info['releaseDate'])
    worksheet2.write(3, 0, 'App最近更新日期')
    worksheet2.write(3, 1, app_info['currentVersionReleaseDate'])
    worksheet2.write(5, 2, 'App评分')
    worksheet2.write(6, 0, '评分总人数')
    worksheet2.write(6, 1, app_rr_info['rateCount'])
    worksheet2.write(6, 3, '平均评分')
    worksheet2.write(6, 4, app_rr_info['rateAvg'])
    worksheet2.write_row('A9', ['1星', '2星', '3星', '4星', '5星'])
    worksheet2.write_row('A10', app_rr_info['rateList'])
    worksheet2.write(11, 0, '评论总数')
    worksheet2.write(11, 1, app_rr_info['reviewsNum'])
    workbook.close()
    print('Done!')

# ---------------------------------------------------
# this function is to link all the funtion above
# one argument: appid
# ---------------------------------------------------
def main_get(appid):
    app_info = get_app_info(appid)
    app_rr_info = get_app_rate_reviewnum(appid)
    app_review_all = get_app_review_all(appid, app_rr_info['reviewsNum'])
    app_info_to_excel(app_info, app_rr_info, app_review_all)


# --------------------------------------
# if get single app comment ,use this
# --------------------------------------
def get_single_app_comment():
    appid = input('input id:')
    main_get(appid)

get_single_app_comment()

# --------------------------------------------------------
# if get many app comment one time, you can use code blow
# --------------------------------------------------------
#
# app_list = ['447551320','627392939','453691481','1104151787'] #you can add app id to this list
# for single_app in app_list:
#     print('getting app ' + str(single_app) + ' comment...')
#     main_get(single_app)
#     print('getting app ' + str(single_app) + ' comment Done!!!\n')
# print('All app comment got!')

