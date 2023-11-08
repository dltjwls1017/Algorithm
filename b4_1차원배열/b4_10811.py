n, m = map(int, input().split())
bag = [i for i  in range(1, n+1)]
temp = []
 
for _ in range(m):
    i, j = map(int, input().split())
    # temp =  bag[i-1:j]
    # temp.reverse()
    # bag[i-1:j] = temp
    bag[i-1:j].reverse()

print(" ".join(map(str, bag)))  # 1 2 1 1 0
# for x in range(n):
#   print(bag[x],end=" ")