def solution(a,b):
    total = 0
    for i in range(a,b+1):
        total += i
        
    if a > b :
        for j in range(b,a+1):
            total += j
    return total