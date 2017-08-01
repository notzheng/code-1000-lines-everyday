import requests

cookies = {
    'traceExt': 'campaign=CHNgoogle323&adid=index',
    'StartCity_Pkg': 'PkgStartCity=477',
    '_abtest_userid': '292e11cf-4df6-4782-9560-37359ee02047',
    'Union': 'OUID=000401app-&AllianceID=293917&SID=1001219&SourceID=&Expires=1500200199372',
    'adscityen': 'Wuhan',
    'Customer': 'HAL=ctrip_gb',
    'ASP.NET_SessionId': 'i4ripljf1dv1zmq4dpanbznk',
    'GUID': '09031011311148741758',
    'HotelCityID': '1split%E5%8C%97%E4%BA%ACsplitBeijingsplit2017-07-15split2017-07-16split0',
    '_bfa': '1.1499590444932.2uuo7m.1.1500056958985.1500060126612.13.38.228032',
    '_bfs': '1.3',
    'HotelDomesticVisitedHotels1': '479844=0,0,4.4,2877,/t1/hotel/7000/6179/0dcc646bb8d2463ea2e2b5524501d790.jpg,&1008154=0,0,4.4,1418,/hotel/99000/98028/6afc0888f623437d93c0ba9826fe5805.jpg,&433114=0,0,4.6,8303,/hotel/19000/18895/7470681c09b643f984c65cb13a930b0d.jpg,&436525=0,0,4.3,1636,/fd/hotel/g3/M09/9D/7E/CggYGVaga5uAYt2wAA9VI-xD900511.jpg,&691682=0,0,4.4,5844,/fd/hotel/g4/M08/12/01/CggYHFXepUuAJmRUAAqGdhCANDQ642.jpg,&436916=0,0,4.4,6001,/hotel/58000/57689/252A20BD-E641-48C8-8D95-66121841295A.jpg,',
    'page_time': '1500048304245%2C1500048307826%2C1500048318415%2C1500048322998%2C1500048575380%2C1500048749274%2C1500048752594%2C1500052747453%2C1500052750367%2C1500052754068%2C1500054189045%2C1500054288138%2C1500056249656%2C1500056257586%2C1500056261482%2C1500056264280%2C1500056269037%2C1500056960978%2C1500056964196%2C1500056968666%2C1500056988573%2C1500057104026%2C1500060127937%2C1500061218691%2C1500061337072',
    '_RF1': '58.19.3.78',
    '_RSG': 'bOaKopp2B.FZhSdMe0b_cB',
    '_RGUID': 'ff8b0b3c-f252-4625-b9bf-940a169dcae3',
    '_ga': 'GA1.2.1297327209.1499590448',
    '_gid': 'GA1.2.1654679955.1500048305',
    '__zpspc': '9.7.1500060129.1500061339.3%231%7C%7C%7C%7C%7C%23',
    '_jzqco': '%7C%7C%7C%7C1500048305261%7C1.559178628.1499590448093.1500061219482.1500061339136.1500061219482.1500061339136.undefined.0.0.34.34',
    'MKT_Pagesource': 'PC',
    'appFloatCnt': '28',
    '_bfi': 'p1%3D102002%26p2%3D102002%26v1%3D32%26v2%3D24',
}

headers = {
    'Origin': 'http://hotels.ctrip.com',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Cache-Control': 'max-age=0',
    'Referer': 'http://hotels.ctrip.com/hotel/beijing1',
    'Connection': 'keep-alive',
    'If-Modified-Since': 'Thu, 01 Jan 1970 00:00:00 GMT',
}

data = [
  ('__VIEWSTATEGENERATOR', 'DB1FBB6D'),
  ('cityName', '%E5%8C%97%E4%BA%AC'),
  ('StartTime', '2017-07-15'),
  ('DepTime', '2017-07-16'),
  ('txtkeyword', ''),
  ('Resource', ''),
  ('Room', ''),
  ('Paymentterm', ''),
  ('BRev', ''),
  ('Minstate', ''),
  ('PromoteType', ''),
  ('PromoteDate', ''),
  ('operationtype', 'NEWHOTELORDER'),
  ('PromoteStartDate', ''),
  ('PromoteEndDate', ''),
  ('OrderID', ''),
  ('RoomNum', ''),
  ('IsOnlyAirHotel', 'F'),
  ('cityId', '1'),
  ('cityPY', 'beijing'),
  ('cityCode', '010'),
  ('cityLat', '39.910532922919'),
  ('cityLng', '116.41378402103'),
 # ('positionArea', ''),
 # ('positionId', ''),
 # ('keyword', ''),
 # ('hotelId', ''),
  ('htlPageView', '0'),
  ('hotelType', 'F'),
  ('hasPKGHotel', 'F'),
  ('requestTravelMoney', 'F'),
  ('isusergiftcard', 'F'),
  ('useFG', 'F'),
 # ('HotelEquipment', ''),
  ('priceRange', '-2'),
  #('hotelBrandId', ''),
  ('promotion', 'F'),
  ('prepay', 'F'),
  ('IsCanReserve', 'F'),
  ('OrderBy', '99'),
 # ('OrderType', ''),
  #('k1', ''),
  #('k2', ''),
 # ('CorpPayType', ''),
  #('viewType', ''),
  ('checkIn', '2017-07-15'),
  ('checkOut', '2017-07-16'),
  #('DealSale', ''),
  #('ulogin', ''),
  ('hidTestLat', '0%7C0'),
  #('AllHotelIds', '691682%2C608345%2C431623%2C433114%2C1008154%2C939388%2C452197%2C479844%2C482534%2C1419816%2C426748%2C2226967%2C5389632%2C4536895%2C374786%2C1725911%2C444199%2C2277604%2C452251%2C1722447%2C1249518%2C1609664%2C456444%2C1836273%2C1419860'),
 # ('psid', ''),
  ('HideIsNoneLogin', 'T'),
  ('isfromlist', 'T'),
  ('ubt_price_key', 'htl_search_result_promotion'),
  #('showwindow', ''),
  #('defaultcoupon', ''),
  ('isHuaZhu', 'False'),
 # ('hotelPriceLow', ''),
  ('htlFrom', 'hotellist'),
  # ('unBookHotelTraceCode', ''),
  # ('showTipFlg', ''),
  # ('hotelIds', '691682_1_1,608345_2_1,431623_3_1,433114_4_1,1008154_5_1,939388_6_1,452197_7_1,479844_8_1,482534_9_1,1419816_10_1,426748_11_1,2226967_12_1,5389632_13_1,4536895_14_1,374786_15_1,1725911_16_1,444199_17_1,2277604_18_1,452251_19_1,1722447_20_1,1249518_21_1,1609664_22_1,456444_23_1,1836273_24_1,1419860_25_1'),
  # ('markType', '0'),
  # ('zone', ''),
  # ('location', ''),
  # ('type', ''),
  # ('brand', ''),
  # ('group', ''),
  # ('feature', ''),
  # ('equip', ''),
  # ('star', ''),
  # ('sl', ''),
  # ('s', ''),
  # ('l', ''),
  # ('price', ''),
  # ('a', '0'),
  # ('keywordLat', ''),
  # ('keywordLon', ''),
  # ('contrast', '0'),
  ('page', '2'),
  # ('contyped', '0'),
  # ('productcode', ''),
]

r = requests.post('http://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx', headers=headers, cookies=cookies, data=data)


print(r.json())