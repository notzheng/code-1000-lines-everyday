import requests

headers = {
    'accept-encoding': 'gzip, deflate, br',
    'x-requested-with': 'XMLHttpRequest',
    'accept-language': 'en-US,en;q=0.8',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'referer': 'https://s.fliggy.com/vacation/list.htm?spm=181.60539.a1zme.5.6df63666hmJ1uT&mq=%E6%97%A5%E6%9C%AC&itemOrderEnum=DEFAULT&orderDirEnum=DESC&searchConditions=&playType=0&_input_charset=utf8',
    'authority': 's.fliggy.com',
    'cookie': 'hng=CN%7Czh-CN%7CCNY; uss=U%2BbEka%2BtScCG4XCwSrgYwYPXC5uckcaBOUcXyG%2BbMZRBFlrp4hcy2wm%2B%2Bw%3D%3D; t=3e591d3eed169dd94b4c0cc2a88f7649; tracknick=%5Cu50BB%5Cu7F3A%5Cu7687%5Cu4E0A; _tb_token_=bpUPSNKFJd9lreO1j0VO; cookie2=1392573d9d71567903083761019052b3; UM_distinctid=15d4a369ac15bc-0dd0a51e10d1dc-30667808-13c680-15d4a369ac2401; cna=yVdYECaa3GoCAYDH/b4wdy3+; isg=AnJyqIi3f-bBT0PafL4SUpOLw774HhppM_msWTxLMyUQzxPJJJJEr1FpyVwJ',
}

params = (
    ('cq', '\u6B66\u6C49'),
    ('mq', '\u65E5\u672C'),
    ('jumpTo', '5'),
    ('itemOrderEnum', 'DEFAULT'),
    ('orderDirEnum', 'DESC'),
    ('searchConditions', ''),
    ('playType', '0'),
    ('_input_charset', 'utf8'),
    ('_ksTS', '1500191032210_1627'),
    ('format', 'json'),
)

r=requests.get('https://s.fliggy.com/vacation/list.htm', headers=headers, params=params)

print(r.json()['page']['totalPage'])
