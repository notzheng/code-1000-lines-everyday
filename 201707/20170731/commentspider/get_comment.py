import requests, xlsxwriter




# def get_hotel_info()

def get_comment(hotel_id):
    all_comment = []
    url = 'https://m.ctrip.com/restapi/soa2/11542/h5-json/getCommentList'
    headers = {
       # '': 'scheme: https',
        'content-type': 'application/json;charset=utf-8',
       # 'content-length': '580',
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/2.5.0',
    }
    pdata_pre = ('{"ClientEnvironmentInfo":"{\\"osver\\":22,\\"wifi\\":\\"1\\",\\"os\\":\\"android\\",\\"swidth\\":\\"360\\",\\"sheight\\":\\"592\\"}",'
            '"HotelId":'+str(hotel_id)+',"HotelStar":3,"HotelType":0,"HotelUserInfo":{"Flag":1},"ModuleSourceType":0,"SearchInfo":{"ControlBitMap":6,"GetTypeBitMap":58,"OperationType":0,"TopSetCommentIdList":""},"ServerSharedData":"","ServiceVersion":0,'
            '"SortingInfo":{"Direction":1,"OrderBy":2,"PageIndex":1,"PageSize":0,"isSelectedByUser":false},'
            '"head":{"auth":"","cid":"32001054710029034073","ctok":"399ddabea5832ab6","cver":"705.000","lang":"01","sauth":"","sid":"8061","syscode":"32"}}')
    r_total = requests.post(url,headers=headers, data=pdata_pre)
    total_json = r_total.json()
    all_comment += total_json['GroupList'][0]['CommentDetailList']
    total_page = total_json['GroupList'][0]['PageTotal']

    for i in range(1,total_page+1):
        pdata = (
        '{"ClientEnvironmentInfo":"{\\"osver\\":22,\\"wifi\\":\\"1\\",\\"os\\":\\"android\\",\\"swidth\\":\\"360\\",\\"sheight\\":\\"592\\"}",'
        '"HotelId":' + str(hotel_id) + ',"HotelStar":3,"HotelType":0,"HotelUserInfo":{"Flag":1},"ModuleSourceType":0,"SearchInfo":{"ControlBitMap":6,"GetTypeBitMap":58,"OperationType":0,"TopSetCommentIdList":""},"ServerSharedData":"","ServiceVersion":0,'
                        '"SortingInfo":{"Direction":1,"OrderBy":2,"PageIndex":'+str(i)+',"PageSize":0,"isSelectedByUser":false},'
                        '"head":{"auth":"","cid":"32001054710029034073","ctok":"399ddabea5832ab6","cver":"705.000","lang":"01","sauth":"","sid":"8061","syscode":"32"}}')
        r_comm = requests.post(url,headers=headers, data=pdata)
        comm_json = r_comm.json()
        comm_list = comm_json['GroupList'][0]['CommentDetailList']
        all_comment += comm_list
        print('第'+str(i)+'波OK～')
    return all_comment


def w_xlsx(all_comment):
    def format_date(date):
        if date =='':
            return ''
        else:
            f_date = date[0:4]+'-'+date[4:6]+'-'+date[6:8]+' '+date[8:10]+':'+date[10:12]+':'+date[12:]
        return f_date
    wk = xlsxwriter.Workbook('6589045.xlsx')
    print('正在写入excel……')
    # hotel_info = wk.add_worksheet('hotelInfo')
    comment = wk.add_worksheet('comment')
    comment_title = ['酒店ID', '评论ID', '评论主题', '内容', '用户昵称', '被点有用数', '评论时间', '入住房间', '入住时间', '入住类型', '总评分', '服务评分',
                     '位置评分', '设施评分', '卫生评分', '用户VIP等级', '用户点评等级', '用户点评总数']
    comment.write_row('A1', comment_title)
    row_c = 1
    for c in all_comment:
        comment.write(row_c, 0, c['HotelId'])
        comment.write(row_c, 1, c['CommentId'])
        comment.write(row_c, 2, c['Subject'])
        comment.write(row_c, 3, c['Content'])
        comment.write(row_c, 4, c['NickName'])
        comment.write(row_c, 5, c['UsefulCount'])
        comment.write(row_c, 6, format_date(c['CreateDate']))
        comment.write(row_c, 7, c['RoomName'])
        comment.write(row_c, 8, format_date(c['checkinDate']))
        comment.write(row_c, 9, c['IdentityText'])
        comment.write(row_c, 10, c['CustPoint'][:3])
        comment.write(row_c, 11, c['ServicePoint'][:3])
        comment.write(row_c, 12, c['RaAtPoint'][:3])
        comment.write(row_c, 13, c['FaclPoint'][:3])
        comment.write(row_c, 14, c['RatPoint'][:3])
        comment.write(row_c, 15, c['VipGrade'])
        comment.write(row_c, 16, c['UserCommentLevel'])
        comment.write(row_c, 17, c['FlagBitMap'])
        row_c += 1
    wk.close()
    print('写入完成！')



if __name__ == '__main__':
    a = get_comment(6589045)
    w_xlsx(a)


