#coding:utf-8
from collections import OrderedDict

#中间平台
mid_info = {
    "ip":"172.16.200.233",
    "mysql_db":"netsale_op_demo",
    "mysql_user":"root",
    "mysql_passwd":"pw1905ns",
    "mid_url":"http://testnetsale.m1905.com:23380/Api"
    }

#第三方app信息
app_info = {
    "app_code":"12",
    "token":"e03aa26a9f85cfa2139468ee0989e4f8"
    }

#影院信息
cinema_info = {
    "cinema_id":"42",
    "cinema_code":"10000142",
    "ip":"192.168.3.142",
    "mysql_db":"tms",
    "mysql_user":"root",
    "mysql_passwd":"123456"
    }

#147信息
cinema_147 = {
    "cinema_code":"10000147",
    "ip":"192.168.3.147",
    "mysql_db":"tms",
    "mysql_user":"root",
    "mysql_passwd":"123456"
    }

#集团信息
center_info = {
    "ip":"192.168.3.140",
    "mysql_db":"tcenter",
    "mysql_user":"root",
    "mysql_passwd":"123456"
    }

#xml响应信息
resp_code = {
    "0":u"请求正确,并且有数据",
    "1":u"请求正确,没有数据",
    "100001":u"参数格式错误",
    "100101":u"参数为空",
    "100201":u"用户不存在",
    "100301":u"签名验证失败",
    "100401":u"锁定座位失败",
    "100402":u"座位与价格长度不匹配",
    "100403":u"参数不能为空",
    "100404":u"价格不匹配",
    "100405":u"订单号重复",
    "100406":u"排期id与影院不匹配",
    "100407":u"部分座位已被锁定",
    "100408":u"排期已开始，停止售卖",
    "100409":u"座位不存在,请同步影厅座位",
    "100410":u"与锁座座位不一致",
    "100501":u"解锁失败",
    "100503":u"订单号不存在",
    "100504":u"订单已售出",
    "100505":u"订单已解锁",
    "100506":u"订单已退票",
    "100507":u"订单已出票",
    "100601":u"订单支付失败",
    "100603":u"订单状态已更改,不能出售",
    "100604":u"订单不存在",
    "100701":u"增加通知url失败",
    "100801":u"影院未返回数据",
    "100901":u"退票订单不存在",
    "100902":u"打印编号错误",
    "100903":u"退票失败",
    "200001":u"权限受限",
    "300001":u"由于网路问题导致此影院不可用",
    "800001":u"卖品列表获取失败",
    "800002":u"卖品订单查询未响应",
    "800003":u"卖品订单查询失败",
    "800004":u"下单失败",
    "800005":u"订单号参数缺失",
    "800006":u"重复订单",
    "800007":u"库存不足",
    "800008":u"订单金额不符",
    "800009":u"卖品推荐列表获取失败",
    "800011":u"会员卡扣款失败",
    "800012":u"卖品分类列表获取失败",
    "800013":u"卖品退货失败",
    "800014":u"卖品价格与数量不一致",
    "800015":u"卖品价格不匹配",
    "800016":u"订单详情错误",
    "800017":u"会员卡号或密码为空",
    "900001":u"会员卡信息获取失败",
    "900002":u"会员卡场次价格获取失败",
    "900003":u"会员卡扣款失败",
    "900005":u"会员卡密码错误",
    "900006":u"会员卡卡号不存在",
    "900007":u"会员卡状态不可用",
    "900008":u"会员卡类型等级信息获取失败",
    "900009":u"会员卡开卡失败",
    "900010":u"会员卡充值失败",
    "900011":u"充值订单重复提交",
    "900012":u"最低限价不匹配",
    "900015":u"没有查询到数据",
    "900016":u"获取失败",
}
