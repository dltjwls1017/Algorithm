a, b = map(int, input().split())
# 바구니 갯수 a개
# 앞으로 총 b줄

arr =[0] * a
for _ in range(b):
    i, j, k = map(int, input().split())
    for index in range(i-1, j):
        arr[index]=k

# print(arr) => [1, 2, 1, 1, 0]
print(" ".join(map(str, arr)))