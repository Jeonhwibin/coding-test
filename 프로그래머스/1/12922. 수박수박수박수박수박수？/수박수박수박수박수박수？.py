def solution(n):
    watermelon = ''
    for i in range(n):
        if i % 2 == 0 :
            watermelon += '수'
        elif i % 2 == 1:
            watermelon += '박'
        else:
            watermelon +='수'
    return watermelon
        