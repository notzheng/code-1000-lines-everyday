import requests
from bs4 import BeautifulSoup


def get_html(yourname):
    cookies = {
        'ASP.NET_SessionId': '3ex04fzycuo0lv55ro1qkaig',
    }

    headers = {
        'Host': '172.16.0.2',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://172.16.0.2',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'http://172.16.0.2/Find_xs_xh.aspx',
        'Accept-Language': 'en-US,en;q=0.8',
    }

    data = [
        ('__EVENTTARGET', 'ctl00$Main$Button1'),
        ('__EVENTARGUMENT', ''),
        ('__VIEWSTATE',
         '/wEPDwUKMTA3NjM0NTY2NQ9kFgJmD2QWAgIDD2QWAgIBEDwrAA0CAA8WAh4LXyFEYXRhQm91bmRnZAwUKwACBQMwOjAUKwACFg4eBFRleHQFBuS4u+mhtR4FVmFsdWUFBuS4u+mhtR4LTmF2aWdhdGVVcmwFDS9EZWZhdWx0LmFzcHgeB0VuYWJsZWRnHgpTZWxlY3RhYmxlZx4IRGF0YVBhdGgFDS9kZWZhdWx0LmFzcHgeCURhdGFCb3VuZGcUKwAFBQ8wOjAsMDoxLDA6MiwwOjMUKwACFg4fAQUG6aG555uuHwIFBumhueebrh8DBQ0vUHJvamVjdC5hc3B4HwRnHwVnHwYFDS9wcm9qZWN0LmFzcHgfB2dkFCsAAhYOHwEFBuiBjOW3pR8CBQbogYzlt6UfAwUOL0VtcGxveWVlLmFzcHgfBGcfBWcfBgUOL2VtcGxveWVlLmFzcHgfB2dkFCsAAhYOHwEFBuWtpueUnx8CBQblrabnlJ8fAwUNL1N0dWRlbnQuYXNweB8EZx8FZx8GBQ0vc3R1ZGVudC5hc3B4HwdnZBQrAAIWDh8BBQblkI7li6QfAgUG5ZCO5YukHwMFDy9Mb2dpc3RpY3MuYXNweB8EZx8FZx8GBQ8vbG9naXN0aWNzLmFzcHgfB2dkZGRkbUXuL8QRHL+2Vs15KXE8cgLZm5k='),
        ('ctl00$Main$Text1', yourname),
        ('__EVENTVALIDATION', '/wEWAwLA1oX+AQLik6LgDgKt2aDzBwZICglx5okpLYOEKmHO3lKCFohW'),
    ]

    r = requests.post('http://172.16.0.2/Find_xs_xh.aspx', headers=headers, cookies=cookies, data=data)

    return r.text


def parse_html(html):
    h = BeautifulSoup(html, 'lxml')
    namelist = []
    tr = h.find_all('tr', style='')
    for t in tr:
        td = t.find_all('td')
        singlename = {
            'sno': td[0].get_text(),
            'name': td[1].get_text(),
            'school': td[2].get_text()
        }
        namelist.append(singlename)

    return namelist


print(parse_html(get_html('郑健')))
