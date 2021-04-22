high = 0
bt = 3
ws = 2
day = 0
while high < 20:
    day = day + 1
    high = high + bt
    if high == 20:
        print("第",day,"天爬出")
    else:
        high = high - ws