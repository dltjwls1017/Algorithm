# import sys

n = int(input())
for i in range(n):
    a, str = input().split()
    for j in range(len(str)):
        print(str[j]*int(a), end='')
    print('')