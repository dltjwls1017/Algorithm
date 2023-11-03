# x 좌표 입력
x = int(input())

# y 좌표 입력
y = int(input())

# 사분면 판단
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)
