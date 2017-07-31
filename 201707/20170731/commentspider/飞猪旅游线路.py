# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 13:55:03 2017

@author: 龙城斗
"""

import requests,json,xlsxwriter

headers = {
    'accept-encoding': 'gzip, deflate, br',
    'x-requested-with': 'XMLHttpRequest',
    'accept-language': 'en-US,en;q=0.8',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
   # 'referer': 'https://s.fliggy.com/vacation/list.htm?spm=181.60539.a1zme.5.6df63666hmJ1uT&mq=%E6%97%A5%E6%9C%AC&itemOrderEnum=DEFAULT&orderDirEnum=DESC&searchConditions=&playType=0&_input_charset=utf8',
    'authority': 's.fliggy.com',
  'cookie': 't=bab46ee927f1307b29c8a7ad0f0ae71f; _tb_token_=aSMQsPymHkHA4nldrnX3; cookie2=1e9c3eb653024adc0ad9e3d9bb51010f; cna=0kryEekGCSwCATowbq1nIdvm; isg=AtnZ9IJF5CN78bi3N-f5wEcK6MMfebkNLKQ3NPuOJoBcAviUQ7Rm6FSacvCP'}

citys=['北京','上海','广州','深圳','成都','杭州','南京','天津','武汉','厦门','沈阳','青岛','西安','重庆','昆明','长沙']
destinations=['韩国','香港','台湾','日本','东南亚','马尔代夫','美国','欧洲','澳新']
line_count=[]
p = 0
#获得旅游线路总数
for each_city in citys:
    line_count_city=[]
    for each_dest in destinations:
        try:
            params = (
                    ('cq', each_city.encode('utf-8')),
                    ('mq', each_dest.encode('utf-8')),
                    ('jumpTo', '1'),
                    ('itemOrderEnum', 'DEFAULT'),
                    ('orderDirEnum', 'DESC'),
                    ('searchConditions', ''),
                    ('playType', '0'),
                    ('_input_charset', 'utf8'),
                    ('format', 'json'),
                )
            page=requests.get('https://s.fliggy.com/vacation/list.htm', headers=headers, params=params)
            total_page=page.json()['page']['totalPage']
            print('哈'*p)
            p+=1
            params_last = (
                    ('cq', each_city.encode('utf-8')),
                    ('mq', each_dest.encode('utf-8')),
                    ('jumpTo',str(total_page)),
                    ('itemOrderEnum', 'DEFAULT'),
                    ('orderDirEnum', 'DESC'),
                    ('searchConditions', ''),
                    ('playType', '0'),
                    ('_input_charset', 'utf8'),
                    ('format', 'json'),
                )
            page_last=requests.get('https://s.fliggy.com/vacation/list.htm', headers=headers, params=params_last)
            line_count_city.append(len(page_last.json()['itemList'])+(total_page-1)*40)
            print(len(page_last.json()['itemList'])+(total_page-1)*40)
        except:
            line_count_city.append(0)
    line_count.append(line_count_city)
print(line_count)    
#写入excel表
'''save_path='C:\\Users\\Administrator\\Desktop\\线路数据数数\\飞猪汇总数据.xlsx'
wk=xlsxwriter.Workbook(save_path)
sheet1=wk.add_worksheet('飞猪-自由行')
for each in range(0,16):
    sheet1.write_column(1,each,line_count[each])
wk.close()'''


