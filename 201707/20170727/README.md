# 校园一卡通接口分析

不小心把代码删了**难受**，等回学校再补上吧。。。

## 登陆









## 挂失

### 接口地址

### 请求头

### 请求体

### 返回数据

```json


//网络故障，推测是系统对账时间
{
  "IsSucceed": false,
  "Msg": null,
  "RMsg": "一卡通网络故障",
  "Obj": null,
  "Obj2": null
}
```



## 修改密码

### 接口地址

```
http://card.cug.edu.cn/User/MendQueryPasswd
```

### 请求头

```javascript
Cookie = {
  "hallticket" : "登录时返回的 cookie 中获得"
}
```

### 请求体

```json
{
  "acc": "卡号",
  "pwd": "原密码",
  "npwd": "新密码",
  "json": true
}
//备注：
//1.新旧密码可以相同，返回修改成功数据
```

### 返回数据

```json
//成功
{
  "IsSucceed": true,
  "Msg": null,
  "RMsg": "密码修改成功",
  "Obj": null,
  "Obj2": null
}

//失败
{
  "IsSucceed": false,
  "Msg": null,
  "RMsg": "账户密码错误",
  "Obj": null,
  "Obj2": null
}
```

