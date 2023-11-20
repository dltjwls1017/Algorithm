def cal(arr):
    score = 0
    total = 0

    for s in arr:
        if s == 'O':
            score += 1  # 맞은 점수만 누적 카운트
            total += score
        else:
            score = 0   # 틀리면 0으로 리셋
            
    return total
    
n = int(input())

for _ in range(n):
    arr = input()
    result = cal(arr)
    print(result)