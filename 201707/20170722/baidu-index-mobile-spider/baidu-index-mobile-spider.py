import requests
import datetime
from datetime import timedelta
import xlsxwriter
import time


def get_data(word, region):
    index_url = 'http://index.baidu.com/Interface/Newwordgraph/getIndex'

    password_url = 'http://index.baidu.com/Interface/api/ptbk'

    cookies = {
        # 'searchtips': '1',
        # 'bdshare_firstime': '1499529040366',
        # 'BAIDUID': '7504D5DA00D90E90529203D878BE342B:FG=1',
        # 'cflag': '15%3A3',
        # 'PSTM': '1500634833',
        # 'BIDUPSID': '970F1C338BB3B8167636C4E87261D8FE',
        # 'CHKFORREG': '42b42c16859f2eff3b26bb5f3440777f',
        # 'BDRCVFR[M7pOaqtZgJR]': 'I67x6TjHwwYf0',
        # 'PSINO': '2',
        # 'H_PS_PSSID': '1438_21110_20718',
        # 'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
        # 'UM_distinctid': '15d651d4c312c3-0678de685a28ce-574e6e46-4a640-15d651d4c323cd',
        # 'CNZZDATA1261825573': '1114474011-1493350587-https%253A%252F%252Fwww.baidu.com%252F%7C1493350587',
        # 'Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc': '1499244616,1500639964,1500639993,1500640025',
        # 'Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc': '1500657231',
        'BDUSS': 'Your BDUSS',
    }

    headers = {
       # 'Accept-Encoding': 'gzip, deflate',
        #'Accept-Language': 'en-US,en;q=0.8',
        #'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
        #'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
       # 'Accept': 'application/json, text/plain, */*',
        #'Referer': 'http://index.baidu.com/baidu-index-mobile/',
       # 'X-Requested-With': 'XMLHttpRequest',
        #'Connection': 'keep-alive',
    }

    index_params = {
        'region': str(region),
        'startdate': '20140101',
        'enddate': '20170721',
        'wordlist[0]': str(word),
    }

    index_r = requests.get(url=index_url, headers=headers, params=index_params, cookies=cookies)

    index_json = index_r.json()

    index_data = index_json['data'][0]['index'][0]
    print(index_data['period'])

    password_params = {
        'uniqid': str(index_json['uniqid'])
    }

    time.sleep(0.05)

    password_r = requests.get(url=password_url, headers=headers, params=password_params, cookies=cookies)

    password_data = password_r.json()['data']

    return_data = {
        'index': index_data,
        'password': password_data
    }

    return return_data


def get_date(start_date, end_date):
    sd = str(start_date)
    ed = str(end_date)
    d1 = datetime.datetime.strptime(sd, '%Y%m%d').date()
    d2 = datetime.datetime.strptime(ed, '%Y%m%d').date()
    delta = d2 - d1
    date_list = [str(d1 + timedelta(days=i)) for i in range(delta.days + 1)]
    return date_list


def decry_data(data, password):
    half_len = len(password) // 2
    pass_dict = {password[i]: password[half_len + i] for i in range(0, half_len)}

    two_date = data['period'].split("|")

    date_list = get_date(two_date[0], two_date[1])


    def decry(sdata):
        s_list = []
        for s in sdata:
            s_list.append(pass_dict[s])
        return "".join(s_list).split(",")

    all = decry(data['_all'])
    pc = decry(data['_pc'])
    wise = decry(data['_wise'])

    decrydata = {
        'date': date_list,
        'all': all,
        'pc': pc,
        'wise': wise
    }

    return decrydata


def write_excel(n, d):
    wk = xlsxwriter.Workbook('百度指数.xlsx')
    ws = wk.add_worksheet(str(n))
    ws.write_row('A1', ['日期', 'PC+移动', 'PC', '移动'])
    ws.write_column('A2', d.date)
    ws.write_column('B2', d.all)
    ws.write_column('C2', d.pc)
    ws.write_column('D2', d.wise)
    wk.close()


if __name__ == '__main__':
    wk = xlsxwriter.Workbook('百度指数.xlsx')

    wordlist = ['哈哈', '呵呵']
    for n in wordlist:
        ws = wk.add_worksheet(str(n))
        dd = get_data(n,0)
        print(n+'~~~~~~~~~')
        d=decry_data(dd['index'],dd['password'])
        ws.write_row('A1', ['日期', 'PC+移动', 'PC', '移动'])
        ws.write_column('A2', d['date'])
        ws.write_column('B2', d['all'])
        ws.write_column('C2', d['pc'])
        ws.write_column('D2', d['wise'])
    wk.close()
