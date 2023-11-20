def factorial(num):
    total = 1
    if num > 0 :
        total = num * factorial(num-1)
    return total

n = int(input())
print(factorial(n)) 
