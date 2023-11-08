n = int(input())
score= list(map(int,input().split()))
m = max(score)

total = 0
for i in range(n):
    score[i] = score[i]/m*100
    total += score[i]
print(total/n)