"""
하찮은 내 코드

n = input().
n.lower()   #모든 문자 소문자로 변경

# 숫자로 주고 아스키코드로 바꿔서 해결하는 방법도.. (내 생각)

arr = 'abcdefghijklmnopqrstuvwxyz'
max = [0, '']

for x in arr:
    temp = 0
    for s in n:
        if x == s:
            temp +=1
    if max[0] < temp:
        max[0] = temp
        max[1] = x
    elif 

"""

word = input().upper()  # 모두 대문자로 변환
new_word = list(set(word)) #중복 제거

# 아! 전체에서 비교하지 말고 중복제거한거랑만 하기
arr = []
for s in new_word:
    # 원래 문자열 중 중복없는 문자열로 찾기
    temp = word.count(s)
    arr.append(temp) # 찾아서 몇 개
    # arr 배열에 중복제서 문자열의 길이만큼 숫자 들어감

if arr.count(max(arr)) > 1:
    print('?')
else:
    n = arr.index(max(arr))
    print(new_word[n])
