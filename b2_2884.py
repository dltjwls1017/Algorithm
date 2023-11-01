a, b = map(int,input().split())
if b-45 < 0:
    a-=1
    b = b + 60 - 45
    if a == -1:
        a = 23

print(a, b)