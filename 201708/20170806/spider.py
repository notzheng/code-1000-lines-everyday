import requests

cookies = {
    'ASP.NET_SessionId': '0ng1e045l5hmqvax1ufdc5vg',
    'tabId': 'ext-comp-1004',
}

headers = {
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://202.114.196.12/xsxkqk.aspx?xh=20151002938',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
}

params = (
    ('kcdm', '6017'), ('xh', '20151002938')

)

r = requests.get('http://202.114.196.12/kcxx.aspx', headers=headers, params=params, cookies=cookies)

print(r.text)
