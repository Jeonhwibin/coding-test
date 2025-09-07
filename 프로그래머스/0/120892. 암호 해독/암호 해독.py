def solution(cipher, code):
    result = ''
    for i in range(len(cipher)):
        if (i+1) % code == 0 :
            result += cipher[i]
    return result