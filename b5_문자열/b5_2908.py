#세 자리수 숫자 두 개 입력 받아 거꾸로
a, b = input().split()

a = int(a[::-1])
b = int(b[::-1])

if a>b :
    print(a)
else:
    print(b)