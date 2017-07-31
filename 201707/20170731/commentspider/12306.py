import requests
import os
from pprint import pprint
from requests.packages.urllib3.exceptions import InsecureRequestWarning


class Train:
    ticket_hash = {
        '商务座': 'swz_num',
        '特等座': 'tz_num',
        '一等座': 'zy_num',
        '二等座': 'ze_num',
        '高级软卧': 'gr_num',
        '软卧': 'rw_num',
        '硬卧': 'yw_num',
        '软座': 'rz_num',
        '硬座': 'yz_num',
        '无座': 'wz_num',
        '其它': 'qt_num'
    }

    def __init__(self, date, from_station, to_station, train_code=None, ticket_type=None):
        # 抑制 12306 自签发的 SSL 证书引发的 warning
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

        self.stationList = self.stationInit()
        self.date = date
        self.from_station = from_station
        self.to_station = to_station
        self.train_code = train_code
        self.ticket_type = ticket_type

    @staticmethod
    def stationInit():
        """
        @bji|北京|BJP|beijing|bj|2
        @拼音缩写三位|站点名称|编码|拼音|拼音缩写|序号
        :return:
        """
        stations = {}
        if not os.path.isfile('station_name.js'):
            res = requests.get(
                'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js',
                verify=False
            )
            with open('station_name.js', 'wb') as fp:
                fp.write(res.content)
        with open('station_name.js', encoding='utf8') as fp:
            data = fp.read()
            data = data.partition('=')[2].strip("'")  # var station_names ='..'
        for station in data.split('@')[1:]:
            items = station.split('|')  # bjb|北京北|VAP|beijingbei|bjb|0
            stations[items[1]] = items[2]
        return stations

    def query(self):
        query_url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}' \
                    '&from_station={}&to_station={}'.format(
            self.date,
            self.stationList[self.from_station],
            self.stationList[self.to_station]
        )
        res = requests.get(query_url, verify=False).text
        pprint(res)
        if res == -1:
            return False
        if not res['data']['flag']:
            return False
        if self.train_code and self.ticket_type:
            for each_train in res['data']['datas']:
                if each_train['station_train_code'] == self.train_code:
                    for each_ticket in self.ticket_type:
                        print(each_ticket + ': ' + each_train[self.ticket_hash[each_ticket]])
        else:
            for each_train in res['data']['datas']:
                print(each_train['station_train_code'])


t = Train('2016-08-20', '武汉', '上海南', 'K121', ['硬卧', '软卧', '硬座', '软座', '无座'])
t.query()