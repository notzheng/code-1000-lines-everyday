import requests

cookies = {
   # 'ASP.NET_SessionId': 'r524oilgn252serp5so3qdrc',
    'hallticket': '5B6BA0E6D0E542E797A78B12EE101197',
    #'username': '20151003873',
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

r=requests.post('http://202.114.200.80/User/GetCardInfoByAccountNoParm', headers=headers, cookies=cookies, data=data)

print(r.status_code)

print(r.json())