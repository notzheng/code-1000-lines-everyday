import requests,base64,json
def login():
    username = input('输入学号：')
    pword = input('输入密码：')
    password = base64.b64encode(bytes(pword,'utf-8')).decode()
    cookies = {
       # 'ASP.NET_SessionId': 'r524oilgn252serp5so3qdrc',
        'username': username,
    }

    headers = {
        'Origin': 'http://202.114.200.80',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'http://202.114.200.80/Phone/Login',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }

    data = [
      ('sno', username),
      ('pwd', password),
      ('remember', '1'),
      ('uclass', '1'),
      ('json', 'true'),
    ]

    r = requests.post('http://card.cug.edu.cn/Phone/Login', headers=headers, cookies=cookies, data=data)

    return r.cookies['hallticket']



def get_money(hallticket):


    url = 'http://202.114.200.80/User/GetCardInfoByAccountNoParm'
    cookies = {
        # 'ASP.NET_SessionId': 'r524oilgn252serp5so3qdrc',
        'hallticket': hallticket,
        # 'username': '20151003873',
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
        ('json', 'true'),
    ]

    r = requests.post(url=url, headers=headers, cookies=cookies, data=data)

    r_json = r.json()
    msg = json.loads(r_json['Msg'])

    print(msg['query_card']['card'][0]['name'])
    balance = str(int(msg['query_card']['card'][0]['db_balance'])/100)
    print(balance+'元')

def get_hisory_list(hallticket):
    url = 'http://card.cug.edu.cn/Report/GetPersonTrjn'

    cookies = {
        'username': '20151002938',
        'hallticket': hallticket,
    }

    headers = {
        'Origin': 'http://card.cug.edu.cn',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'http://card.cug.edu.cn/Page/Page',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }

    data = [
        ('sdate', '2015-08-01'),
        ('edate', '2017-07-20'),
      #  ('account', '109927'),
        ('page', '13'),
        ('rows', '15'),
    ]

    r = requests.post(url=url,headers=headers, cookies=cookies, data=data)
    r_json = r.json()
    print(r_json)


# print('密码默认身份证后六位')
print()
#  get_hisory_list(login())
