#有以下一个列表，求其中是5的倍数的和
a = [1,5,21,30,15,9,30,24]
n=0
sum=0
while n < len(a) :
   if a[n]%5 == 0 :
       sum=a[n]+sum
       n = n + 1
   elif 0!=a[n]%5:
       n = n + 1
print("5的倍数总和：", sum)






















print()







