a = int(input())
b = int(input())
c = int(input())
total = a*b*c
print(total)
print(str(total))
arr = '0123456789'
for x in arr:
    count = 0
    for s in str(total):
        if s == x:
            count += 1
    print(count)