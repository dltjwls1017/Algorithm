# arr=[]
# for i in range(9):
#     arr[i] = int(input())
# Max = max(arr)
# print(Max)
# num=0
# for i in range(9):
#     if Max == arr[i]:
#         print(num+1)

# Help
arr = []
for i in range(9):
    arr.append(int(input()))
print(max(arr))
print(arr.index(max(arr))+1)

