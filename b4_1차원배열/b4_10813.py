n, m = map(int, input().split())
arr = list(range(1,n+1))

for _ in range(m):
    i, j = map(int, input().split())
    x = arr[i-1]
    arr[i-1] = arr[j-1]
    arr[j-1] = x

print(" ".join(map(str, arr)))  # 1 2 1 1 0