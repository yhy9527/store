
count=0
sum=0
n=0
while True:
    num = input("请输入10个数字：")
    num = int(num)
    if count < 9:
        count = count + 1
        sum = num + sum
    if num > n:
        n=num
    elif count == 9:
        sum = num + sum
        print(" 10个数字和：",sum,"\n","平均数：",sum/10,"\n","最大数是：",n)
        break



