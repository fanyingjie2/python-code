#!/usr/bin/env python3
#-*- coding: utf-8 -*-

s = "13.231.45.60$$Geth-test02$$erc20API$$2019-09-23 10:55:12$$出错重启了一次"
sl = s.split("$$")
print(",".join(sl))
sms_info = "服务器{0[0]}（{0[1]}）的{0[2]}在{0[3]}发生错误：{0[4]}".format(sl)
print(sms_info)