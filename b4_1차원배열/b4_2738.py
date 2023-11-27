n, m = map(int, input().split())
a, b = [], []

for i in range(n):
        a.append(list(map(int, input().split())))

for i in range(n):
        b.append(list(map(int, input().split())))

for i in range(n): # n번 반복
    for j in range(m): # m번 반복
        print(a[i][j] + b[i][j], end = " ") # a와 b의 각각의 값을 더한 값을 출력
    print() # 줄바꿈