x = int(input())
n = int(input())
total = 0 
for i in range(n):
    a,b = map(int, input().split())
    total = total + a*b
if x==total:
    print('Yes')
else:
    print("No")