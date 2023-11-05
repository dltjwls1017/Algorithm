#01_ 구구단

N = int(input())
for i in range(1, 10, 1):
    print('{} * {} = {}'.format(N, i, N*i))