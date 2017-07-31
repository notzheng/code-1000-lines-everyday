import requests,json
cookies = {

    'hallticket': '4054D880BB664787A4FF01852B40191A',
    'username':'20151002938'
}
#
# headers = {
#     'Origin': 'http://card.cug.edu.cn',
#     'Accept-Encoding': 'gzip, deflate',
#     'Accept-Language': 'en-US,en;q=0.8',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
#     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'Referer': 'http://card.cug.edu.cn/Page/Page',
#     'X-Requested-With': 'XMLHttpRequest',
#     'Connection': 'keep-alive',
# }
#
# data = [
#     # ('sdate', '2017-06-20'),
#     # ('edate', '2017-07-20'),
#     ('account', '109928'),
#     ('page', '1'),
#     ('rows', '2000'),
# ]
#
# r = requests.post('http://card.cug.edu.cn/Report/GetPersonTrjn', headers=headers, cookies=cookies, data=data)
# print(r.text)



def get_money():


    url = 'http://202.114.200.80/User/GetCardInfoByAccountNoParm'
    cookies = {
        # 'ASP.NET_SessionId': 'r524oilgn252serp5so3qdrc',
        'hallticket': '4054D880BB664787A4FF01852B40191A',
        'username': '20151002938',
    }

    headers = {
        'Origin': 'http://202.114.200.80',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'http://202.114.200.80/Page/Page',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }

    data = [
        ('json', 'true')
    ]

    r = requests.post(url=url, headers=headers, cookies=cookies, data=data)

    r_json = r.json()
    msg = json.loads(r_json['Msg'])

    print(msg['query_card']['card'][0]['name'])
    balance = str(int(msg['query_card']['card'][0]['db_balance'])/100)
    print(balance+'元')

get_money()