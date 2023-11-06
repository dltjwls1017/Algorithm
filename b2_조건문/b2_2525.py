a, b = map(int,input().split())
n = int(input())

total = a*60 + b + n
# a = total // 60
# b = total - a*60
a, b = divmod(total, 60)

a = a%24

print(a, b)
