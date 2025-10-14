N = int(input())

# 윤년은 4의 배수이면서 , 100의 배수가 아닐 때 또는 400의 배수일 때

if N % 4 == 0 and N % 100 != 0:
    print(1)
elif N % 4 ==0 and N % 400 ==0 :
    print(1)
else:
    print(0)