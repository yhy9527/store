#羽绒服
yrf="羽绒服"
price_01=253.6
kucun_01=500
list01=[10,69,140,10,10]
#牛仔裤
nzk="牛仔裤"
price_02=86.3
kucun_02=600
list02=[60,72,35,90,60,60,140]
#风衣
fy="风衣"
price_03=96.8
kucun_03=335
list03=[43,25,43,60,43,78]
#皮草
pc="皮草"
price_04=135.9
kucun_04=855
list04=[57,63,24,63]
#T恤
tx="T恤"
price_05=65.8
kucun_05=632
list05=[63,45,129,63,58,48,63]
#衬衫
cs="衬衫"
price_06=49.3
kucun_06=562
list06=[120]
#销售总金额
total=price_01*sum(list01)+price_02*sum(list02)+\
price_03*sum(list03)+price_04*sum(list04)+price_05*sum(list05)+price_06*sum(list06)

print("*******************12月衣服的销售数据查询系统******************")
clothes=input("请输入要查询的衣服：")
if clothes == yrf:
    print(" 12月总销售额：￥",round(total,2),"\n","羽绒服销售额：￥",(price_01*sum(list01)),"\n","销售额占比：",
          "%.2f%%" % (price_01 * sum(list01)/round(total,2)*100))

if clothes == nzk:
    print(" 12月总销售额：￥", round(total, 2), "\n", "牛仔裤销售额：￥", (price_02 * sum(list02)), "\n", "销售额占比：",
          "%.2f%%" % (price_02 * sum(list02) / round(total, 2) * 100))

if clothes == fy:
    print(" 12月总销售额：￥", round(total, 2), "\n", "风衣销售额：￥", (price_03 * sum(list03)), "\n", "销售额占比：",
          "%.2f%%" % (price_03 * sum(list03) / round(total, 2) * 100))

if clothes == pc:
    print(" 12月总销售额：￥", round(total, 2), "\n", "皮草销售额：￥", (price_04 * sum(list04)), "\n", "销售额占比：",
          "%.2f%%" % (price_04 * sum(list04) / round(total, 2) * 100))

if clothes == tx:
    print(" 12月总销售额：￥", round(total, 2), "\n", "T恤销售额：￥", (price_05 * sum(list05)), "\n", "销售额占比：",
          "%.2f%%" % (price_05 * sum(list05) / round(total, 2) * 100))

if clothes == cs:
    print(" 12月总销售额：￥", round(total, 2), "\n", "衬衫销售额：￥", (price_06 * sum(list06)), "\n", "销售额占比：",
          "%.2f%%" % (price_06 * sum(list06) / round(total, 2) * 100))







