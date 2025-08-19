def solution(n):
    
    pizza = 0
    if n <= 7:
        return 1
    elif  n>8:
        pizza += n // 7
        if n % 7 != 0:
            pizza +=1
        return pizza
    