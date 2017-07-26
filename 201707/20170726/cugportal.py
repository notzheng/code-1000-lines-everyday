import requests
s = requests.Session()

    s.get("https://portal.cug.edu.cn/zfca/securitycenter/loginzfca.jsp", verify=False)

    headers = {
        'Origin': 'https://portal.cug.edu.cn',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'Referer': 'https://portal.cug.edu.cn/zfca/securitycenter/loginzfca.jsp',
        'Connection': 'keep-alive',
    }


    data = [
      ('auto', 'true'),
      ('issubmit', 'true'),
      ('username', xh ),
      ('password', password),
      ('losetime', '30'),
      ('savedl', ''),
    ]

    r=s.post('https://portal.cug.edu.cn/zfca/remoteLogin?service=http://portal.cug.edu.cn/portal.do', headers=headers, data=data, verify=False)
