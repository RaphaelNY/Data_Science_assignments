R = int(input("请输入一个正整数R: "))

total = 0

for i in range(1, R + 1):
    total += i

print("整数累加为: {}".format(total))
