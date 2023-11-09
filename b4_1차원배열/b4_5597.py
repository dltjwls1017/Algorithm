# 방법 1 : 입력 숫자를 정렬
# 방법 2 : 제거 ( remove () )

stu = [i for i in range(1, 31)]
for i in range(28):
    num = (int(input()))
    stu.remove(num)

print(min(stu))
print(max(stu))
     