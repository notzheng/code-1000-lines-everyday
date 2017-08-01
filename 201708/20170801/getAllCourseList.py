# -*- coding：gb2312 -*-
from lxml import etree
import requests
import pickle
import time
import warnings
import re
warnings.filterwarnings("ignore")



def get_session_url(xh, password):
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
        ('username', xh),
        ('password', password),
        ('losetime', '30'),
        ('savedl', ''),
    ]
    try:
        s.post('https://portal.cug.edu.cn/zfca/remoteLogin?service=http://portal.cug.edu.cn/portal.do',
               headers=headers,
               data=data, verify=False, timeout=10)
        r = s.get("https://portal.cug.edu.cn/zfca?yhlx=student&login=0122579031373493685&url=xs_main.aspx",
                  verify=False, timeout=10)
        myurl = r.url
        rurl = re.findall(r'http://(.+)/', str(myurl))[0]
        return s.cookies['ASP.NET_SessionId'],rurl
    except:

        print( "网络错误")
        return False

a = get_session_url('20151003873','181213')
print(a)

cookies = {
    'ASP.NET_SessionId': a[0]
}

r1 = requests.get(url='http://'+str(a[1])+'/jxrwcx.aspx?xh=20151003873', cookies=cookies)

url = 'http://'+a[1]+'/jxrwcx.aspx?xh=20151003873'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': a[1],
    'Origin': 'http://'+a[1],
    'Referer': 'http://'+a[1]+'/xs_main.aspx?xh=20151003873',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}

pdata = {'__EVENTTARGET': '', '__EVENTARGUMENT': '', 'ddlXY': '', 'ddlJS': '', 'kcmc': '',
         'ddlXN': '2014-2015', 'ddlXQ': '1', 'DropDownList1': 'kcmc', 'TextBox1': ''   }
pdata['Button1'] = ' 查 询 '.encode('gb2312')
pdata['__VIEWSTATE'] = etree.HTML(r1.text).xpath('//*[@name="__VIEWSTATE"]/@value')[0]

def courseinfo(r):
    html = etree.HTML(r)
    table = html.xpath('//*[@id="DBGrid"]/tr')
    headers = ['status', 'coursename', 'score', 'testtype', 'coursetype', 'teacher', 'chooiceid', 'weeks', 'time',
               'place', 'school', 'classes']
    courselist = table[1:-1]
    # print(courselist)
    final_list = []
    for course in courselist:
        courseinfo = course.xpath('td')
        infolist = []
        for info in courseinfo:
            if 'title' in info.attrib.keys():
                infolist.append(info.attrib['title'])
            else:
                infolist.append(info.text)
            infodict = dict(zip(headers, infolist))
        final_list.append(infodict)
    return final_list

def postdict(cc):
    html = etree.HTML(cc)
    post_dict = {
        '__EVENTARGUMENT': '',
        'ddlXY': '',
        'ddlJS': '',
        'kcmc': '',
        'ddlXN': '2014-2015',
        'ddlXQ': '1',
        'DropDownList1': 'kcmc',
        'TextBox1': ''
        # 'Button1': ' 查 询 '
    }
    viewstate = html.xpath('//*[@name="__VIEWSTATE"]/@value')[0]
    post_dict['__VIEWSTATE'] = viewstate
    try:
        nextpageid = html.xpath('//td[@colspan="19"]/span/following-sibling::a[1]/@href')[0][25:-5]
        nextpage =html.xpath('//td[@colspan="19"]/span')[0].text
        print(nextpage)
        nextpageid = nextpageid.replace('$',':')
        post_dict['__EVENTTARGET'] = nextpageid
        # print(nextpageid)
        return post_dict
    except:
        return False

rp1 = requests.post(url=url, headers=headers, cookies=cookies, data=pdata)


allcourseinfo = []

ppdata = postdict(rp1.text)

while True:
    rp = requests.post(url=url, headers=headers, cookies=cookies, data=ppdata)
    allcourseinfo += (courseinfo(rp.text))
    ppdata = postdict(rp.text)
    time.sleep(0.05)
    # print(ppdata)
    if not ppdata:
        break

# print(allcourseinfo)
savefile = open('2014-2015-1.pkl','wb')
pickle.dump(allcourseinfo,savefile)
savefile.close()