// 0.Get APPID

//  by searching on Goole or Baidu with keyword "APPname + iTunes"
url = 'https://itunes.apple.com/cn/app/wei-xin/id414478124?mt=8'
APPID = 414478124

// 1.Get App Info -- iTunes search API by apple

//  [url] -- (no header requried) (method = get)
url = 'https://itunes.apple.com/lookup?cc=cn&id={APPID}'
//  [return data(json)] -- (to unserstand this, you can visit https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/#understand )
data = {
	"resultCount": 1,
	"results": [{
		"artistViewUrl": "https://itunes.apple.com/cn/developer/wechat/id614694882?uo=4",
		"artworkUrl60": "http://is2.mzstatic.com/image/thumb/Purple19/v4/74/a1/f3/74a1f3df-ef81-7268-0246-f8f1db1b2845/source/60x60bb.jpg",
		"artworkUrl100": "http://is2.mzstatic.com/image/thumb/Purple19/v4/74/a1/f3/74a1f3df-ef81-7268-0246-f8f1db1b2845/source/100x100bb.jpg",
		"ipadScreenshotUrls": ["http://a1.mzstatic.com/us/r30/Purple91/v4/b9/c2/10/b9c2102e-74c2-6785-13ff-dbd43ba3d8b1/sc1024x768.jpeg", "http://a4.mzstatic.com/us/r30/Purple127/v4/0f/7b/c2/0f7bc27a-9b0c-e0c2-d7d8-d9187a8b0335/sc1024x768.jpeg", "http://a2.mzstatic.com/us/r30/Purple117/v4/60/7b/92/607b9218-e8ca-dbfd-23d4-ba4b65e0d452/sc1024x768.jpeg"],
		"appletvScreenshotUrls": [],
		"artworkUrl512": "http://is2.mzstatic.com/image/thumb/Purple19/v4/74/a1/f3/74a1f3df-ef81-7268-0246-f8f1db1b2845/source/512x512bb.jpg",
		"features": ["iosUniversal"],
		"kind": "software",
		"supportedDevices": ["iPad2Wifi-iPad2Wifi", "iPad23G-iPad23G", "iPhone4S-iPhone4S", "iPadThirdGen-iPadThirdGen", "iPadThirdGen4G-iPadThirdGen4G", "iPhone5-iPhone5", "iPodTouchFifthGen-iPodTouchFifthGen", "iPadFourthGen-iPadFourthGen", "iPadFourthGen4G-iPadFourthGen4G", "iPadMini-iPadMini", "iPadMini4G-iPadMini4G", "iPhone5c-iPhone5c", "iPhone5s-iPhone5s", "iPadAir-iPadAir", "iPadAirCellular-iPadAirCellular", "iPadMiniRetina-iPadMiniRetina", "iPadMiniRetinaCellular-iPadMiniRetinaCellular", "iPhone6-iPhone6", "iPhone6Plus-iPhone6Plus", "iPadAir2-iPadAir2", "iPadAir2Cellular-iPadAir2Cellular", "iPadMini3-iPadMini3", "iPadMini3Cellular-iPadMini3Cellular", "iPodTouchSixthGen-iPodTouchSixthGen", "iPhone6s-iPhone6s", "iPhone6sPlus-iPhone6sPlus", "iPadMini4-iPadMini4", "iPadMini4Cellular-iPadMini4Cellular", "iPadPro-iPadPro", "iPadProCellular-iPadProCellular", "iPadPro97-iPadPro97", "iPadPro97Cellular-iPadPro97Cellular", "iPhoneSE-iPhoneSE", "iPhone7-iPhone7", "iPhone7Plus-iPhone7Plus", "iPad611-iPad611", "iPad612-iPad612", "iPad71-iPad71", "iPad72-iPad72", "iPad73-iPad73", "iPad74-iPad74"],
		"screenshotUrls": ["http://a5.mzstatic.com/us/r30/Purple122/v4/d1/d8/2c/d1d82c14-bb28-3dc4-58a5-476c9a8c0a9c/screen696x696.jpeg", "http://a5.mzstatic.com/us/r30/Purple122/v4/30/0f/bb/300fbb4a-8eb4-52c7-98ad-b6a203d7ea2f/screen696x696.jpeg", "http://a3.mzstatic.com/us/r30/Purple122/v4/0a/d3/e0/0ad3e0a4-71dd-f675-4a3a-7413ffe50646/screen696x696.jpeg", "http://a5.mzstatic.com/us/r30/Purple117/v4/34/99/ec/3499ec44-d017-08d1-3b7b-cc9d216bd333/screen696x696.jpeg", "http://a2.mzstatic.com/us/r30/Purple127/v4/89/5c/8c/895c8c74-3aa7-7781-9c01-67bf36d974dd/screen696x696.jpeg"],
		"isGameCenterEnabled": false,
		"advisories": ["偶尔/轻微的色情内容或裸露"],
		"trackCensoredName": "微信",
		"trackViewUrl": "https://itunes.apple.com/cn/app/%E5%BE%AE%E4%BF%A1/id414478124?mt=8&uo=4",
		"contentAdvisoryRating": "12+",
		"languageCodesISO2A": ["AR", "ZH", "EN", "FR", "DE", "HE", "HI", "ID", "IT", "JA", "KO", "MS", "PL", "PT", "RU", "ZH", "ES", "TH", "ZH", "TR", "VI"],
		"fileSizeBytes": "189603840",
		"sellerUrl": "http://weixin.qq.com",
		"averageUserRatingForCurrentVersion": 4.0,
		"userRatingCountForCurrentVersion": 4208,
		"trackContentRating": "12+",
		"minimumOsVersion": "8.0",
		"currency": "CNY",
		"wrapperType": "software",
		"version": "6.5.9",
		"artistId": 614694882,
		"artistName": "WeChat",
		"genres": ["社交", "效率"],
		"price": 0.00,
		"description": "微信是一款全方位的手机通讯应用，帮助你轻松连接全球好友。微信可以(通\n过SMS/MMS网络)发送短信、进行视频聊天、与好友一起玩游戏，以及分享自己的\n生活到朋友圈，让你感受耳目一新的移动生活方式。\n\n  为什么要使用微信：\n  • 多媒体消息：支持发送视频、图片、文本和语音消息。\n  • 群聊和通话：组建高达500人的群聊和高达9人的实时视频聊天。\n  • 免费语音和视频聊天：提供全球免费的高质量通话。\n  • WeChat Out：超低费率拨打全球的手机或固定电话（目前仅限于部分地区）。\n  • 表情商店：海量免费动态表情，包括热门卡通人物和电影，让聊天变得更生动有趣。\n  • 朋友圈：与好友分享每个精彩瞬间，记录自己的生活点滴。\n  • 隐私保护：严格保护用户的隐私安全，是唯一一款通过TRUSTe认证的实时通讯应用。\n  • 认识新朋友：通过“雷达加朋友”、“附近的人”和“摇一摇”认识新朋友。\n  • 实时位置共享：与好友分享地理位置，无需通过语言告诉对方。\n  • 多语言：支持超过20种语言界面，并支持多国语言的消息翻译。\n  · 微信运动，支持接入Apple Watch 及iPhone健康数据，可通过“WeRun-WeChat”公众号与好友一较高下。\n  • 更多功能: 支持跨平台、聊天室墙纸自定义、消息提醒自定义和公众号服务等。",
		"trackId": 414478124,
		"trackName": "微信",
		"bundleId": "com.tencent.xin",
		"isVppDeviceBasedLicensingEnabled": true,
		"primaryGenreName": "Social Networking",
		"releaseDate": "2011-01-21T01:32:15Z",
		"primaryGenreId": 6005,
		"sellerName": "Tencent Technology (Shenzhen) Company Limited",
		"genreIds": ["6005", "6007"],
		"currentVersionReleaseDate": "2017-06-14T08:39:43Z",
		"releaseNotes": "本次更新\n- 可在微信实验室体验正在探索的功能。\n- 聊天中查找聊天内容时，可以查找文件、图片、链接。\n- 群主可在群成员信息页中，了解对方是如何加入群聊的。\n- 选择图片时，可便捷地调整并预览已选择的内容。\n\n最近更新\n- 新的语音输入，更快更准。\n- 选择照片时，可进行简单的编辑。\n- 看不完的文章，可以先置顶到聊天中。",
		"formattedPrice": "免费",
		"averageUserRating": 4.0,
		"userRatingCount": 758394
	}]
}

/* ----------------------------- */

// 2.Get Rate Data and Reviewcount -- by capturing packets 

// [url] -- (user-agent "itunes" required)  (method = get)
url = 'https://itunes.apple.com/cn/customer-reviews/cc=cn&id{APPID}?dataOnly=true&displayable-kind=11'

header = {
    'user-agent': 'iTunes/12.6.1 (Macintosh; OS X 10.12.5) AppleWebKit/603.2.4'
 }

// [return data(json)] 
data = {
	"adamId": 414478124,
	"clickToRateUrl": "https://userpub.itunes.apple.com/WebObjects/MZUserPublishing.woa/wa/userRateContent?displayable-kind=11&id=414478124",
	"writeUserReviewUrl": "https://userpub.itunes.apple.com/WebObjects/MZUserPublishing.woa/wa/writeUserReview?cc=cn&displayable-kind=11&id=414478124",
	"totalNumberOfReviews": 421726,
	"userReviewsRowUrl": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/userReviewsRow",
	"userReviewsSortOptions": [{
		"sortId": 1,
		"name": "最有帮助"
	}, {
		"sortId": 2,
		"name": "最高评价"
	}, {
		"sortId": 3,
		"name": "最低评价"
	}, {
		"sortId": 4,
		"name": "最新发表"
	}],
	"kindId": 11,
	"kindExtId": "iosSoftware",
	"kindName": "software",
	"saveUserReviewUrl": "https://userpub.itunes.apple.com/WebObjects/MZUserPublishing.woa/wa/saveUserReview?displayable-kind=11",
	"ariaLabelForRatings": "4星",
	"ratingCount": 758394,
	"ratingCountList": [139303, 31864, 51141, 77272, 458814], // 1 star to 5 start
	"ratingAverage": 4,
	"currentVersion": {
		"ariaLabelForRatings": "4星",
		"ratingCount": 4249,
		"ratingCountList": [818, 218, 314, 405, 2494], // 1 star to 5 start
		"ratingAverage": 4
	}
}

// 3.Get Review -- by capturing packets 

// [url] -- (user-agent "itunes" required)  (method = get)
url = 'https://itunes.apple.com/WebObjects/MZStore.woa/wa/userReviewsRow?cc=cn&id=379395415&displayable-kind=11&startIndex=0&endIndex=100&sort=1&appVersion=all'

query_str = {	// some of query_str
        'id': '414478124', // appId in appstore
        'startIndex': '0', // commentNum begin
        'endIndex': '1000',// commentNum end
        'sort': '0',		// sort = 1: most helpful 2: highest rate 3.lowerest 4. lastest 
        'appVersion': 'all' // all: allversion current:current
}

header = {
    'user-agent': 'iTunes/12.6.1 (Macintosh; OS X 10.12.5) AppleWebKit/603.2.4'
 }

// [return data(json)]
// [{},{},{}] = json['userReviewList']

{
  "userReviewList": [
    {
      "userReviewId": "390169394",
      "body": "他们开发的iphoneQQ实在有够烂的。",
      "date": "2011-01-21T04:02:03Z",
      "name": "cnszx",
      "rating": 5,
      "title": "Weixinteam你们去帮下qqteam吧",
      "voteCount": 18,
      "voteSum": 15,
      "isEdited": false,
      "viewUsersUserReviewsUrl": "https://itunes.apple.com/cn/reviews?userProfileId=164843030",
      "voteUrl": "https://userpub.itunes.apple.com/WebObjects/MZUserPublishing.woa/wa/rateUserReview?userReviewId=390169394",
      "reportConcernUrl": "https://userpub.itunes.apple.com/WebObjects/MZUserPublishing.woa/wa/reportAConcernSubmit?cc=cn",
      "reportConcernExplanation": "请提供关于此篇“微信”评论的详细信息。评论作者不会看到您的报告。",
      "customerType": "Customers",
      "reportConcernReasons": [ /* delete it because it's reportConcernReasons */]
    },
    {
      "userReviewId": "390207580",
      "body": "你们才是真正的腾讯控。",
      "date": "2011-01-21T07:58:43Z",
      "name": "皮克车",
      "rating": 5,
      "title": "服了你们了。一边用人家的产品，一边骂人家。很不厚道。",
      "voteCount": 1,
      "voteSum": 0,
      "isEdited": false,
      "viewUsersUserReviewsUrl": "https://itunes.apple.com/cn/reviews?userProfileId=158123598",
      "voteUrl": "https://userpub.itunes.apple.com/WebObjects/MZUserPublishing.woa/wa/rateUserReview?userReviewId=390207580",
      "reportConcernUrl": "https://userpub.itunes.apple.com/WebObjects/MZUserPublishing.woa/wa/reportAConcernSubmit?cc=cn",
      "reportConcernExplanation": "请提供关于此篇“微信”评论的详细信息。评论作者不会看到您的报告。",
      "customerType": "Customers",
      "reportConcernReasons": [ ]
    },
    {
      "userReviewId": "390216680",
      "body": "好",
      "date": "2011-01-21T09:19:46Z",
      "name": "Kōma",
      "rating": 5,
      "title": "好",
      "voteCount": 0,
      "voteSum": 0,
      "isEdited": false,
      "viewUsersUserReviewsUrl": "https://itunes.apple.com/cn/reviews?userProfileId=114715453",
      "voteUrl": "https://userpub.itunes.apple.com/WebObjects/MZUserPublishing.woa/wa/rateUserReview?userReviewId=390216680",
      "reportConcernUrl": "https://userpub.itunes.apple.com/WebObjects/MZUserPublishing.woa/wa/reportAConcernSubmit?cc=cn",
      "reportConcernExplanation": "请提供关于此篇“微信”评论的详细信息。评论作者不会看到您的报告。",
      "customerType": "Customers",
      "reportConcernReasons": [ ]
    }
  ]
}



