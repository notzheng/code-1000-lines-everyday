# -*- coding：gb2312 -*-


import requests
import re
import warnings
from lxml import etree
# do not show warings
warnings.filterwarnings("ignore")


class OneClickToPJ():
    def __init__(self,xh,password):
        self.xh = xh
        self.password = password

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
            s.post('https://portal.cug.edu.cn/zfca/remoteLogin?service=http://portal.cug.edu.cn/portal.do',
                   headers=headers,
                   data=data, verify=False)
            r = s.get("https://portal.cug.edu.cn/zfca?yhlx=student&login=0122579031373493685&url=xs_main.aspx",
                      verify=False)
            return s.cookies['ASP.NET_SessionId'], r.url
        try:
            self.session_url = get_session_url(xh,password)
            self.cookie = {
                'ASP.NET_SessionId':self.session_url[0]
            }
            self.url = self.session_url[1]
            self.ip = self.ip = re.findall(r'http://(.+)/', str(self.url))[0]
            self.waring = False
        except:
            self.waring = "密码错误，请重试"

    def get_course_list(self):
        url = 'http://'+self.ip+'/xsjxpj.aspx'
        cookies = self.cookie
        headers = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
        }

        params = (
            ('xh', self.xh),
        )

        r_html = requests.get(url=url, headers=headers, params=params, cookies=cookies).text
        if "你已经评价过!" in r_html:
            print("已经评价过！")
            return False
        else:
            html = etree.HTML(r_html)
            courses = html.xpath('//*[@id="pjkc"]/option')
            print(len(courses))
            for c in courses:
                print(c.text)
            return r_html

    def post_dict(self,r_html):

        post_dict = {
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            'pjxx': '',
            'txt1': '',
            'TextBox1': 0
        }
        html = etree.HTML(r_html)
        view_state = html.xpath('//*[@name="__VIEWSTATE"]')[0].attrib['value']
        post_dict['__VIEWSTATE'] = view_state
        if "所有评价已完成，现在可以提交" in r_html:
            button = html.xpath('//*[@id="Button2"]')
            post_dict['Button2'] = button[0].attrib['value']
        else:
            button = html.xpath('//*[@id="Button1"]')
            post_dict['Button1'] = button[0].attrib['value'].encode('gb2312')


        pjkc = html.xpath('//*[@id="pjkc"]/option[@selected]')[0].attrib['value']
        post_dict['pjkc'] = pjkc
        o = html.xpath('//*[starts-with(@name, "DataGrid")]')
        many_teachers = 0
        for oo in o:
            if many_teachers <= 2 or many_teachers in [8,10,11,12,20,22,26,30,32]:
                pj = "良".encode('gb2312')
            else:
                pj = "优".encode('gb2312')
            dict_key = oo.attrib['name']
            if 'txt' in dict_key:
                post_dict[dict_key] = ""
            else:
                many_teachers += 1
                post_dict[dict_key] = pj

        # if len(o)>5:
        #     for oo in o:
        #         if many_teachers % 3 == 0:
        #             pj = html.xpath('//*[starts-with(@value, "良")]')[0].text.encode('gb2312')
        #         elif many_teachers % 3 ==1:
        #             pj = html.xpath('//*[starts-with(@value, "优")]')[0].text.encode('gb2312')
        #         else:
        #             pj = html.xpath('//*[starts-with(@value, "中")]')[0].text.encode('gb2312')
        #         dict_key = oo.attrib['name']
        #         if 'txt' in dict_key:
        #             post_dict[dict_key] = ""
        #         else:
        #             many_teachers += 1
        #             post_dict[dict_key] = pj
        #     #pj = html.xpath('//*[starts-with(@value, "优")]')[0].text.encode('gb2312')
        # else:
        #     pj = html.xpath('//*[starts-with(@value, "良")]')[0].text.encode('gb2312')
        #     for oo in o:
        #         dict_key = oo.attrib['name']
        #         if 'txt' in dict_key:
        #             post_dict[dict_key] = ""
        #             # many_teachers += 2
        #         else:
        #             post_dict[dict_key] = pj
        #         pj = html.xpath('//*[starts-with(@value, "良")]')[0].text.encode('gb2312')

        # print(post_dict)

        return post_dict

    def post_pj(self,post_dict):
        url = 'http://' + self.ip + '/xsjxpj.aspx'
        headers = {
            'Origin': url,
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Cache-Control': 'max-age=0',
            'Referer': url+'?'+str(self.xh),
            'Connection': 'keep-alive',
        }
        params = (
            ('xh', self.xh),
        )
        #print(post_dict)
        post = requests.post(url=url,headers=headers, params=params, cookies=self.cookie, data=post_dict)

        return post.text

    def main_pj(self):
        if not self.waring:
            first_get = self.get_course_list()

            if first_get:
                p_dict = self.post_dict(r_html=first_get)
                first_post = self.post_pj(post_dict=p_dict)
                while True:
                    p_dict = self.post_dict(r_html=first_post)
                    first_post = self.post_pj(post_dict=p_dict)
                    if "已完成评价" in first_post:
                        print("完成")
                        return "OK"
        else:
            print(self.waring)

a = OneClickToPJ(20151000000,"000000")


c = a.main_pj()





