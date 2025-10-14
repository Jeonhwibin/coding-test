n = int(input())
for _ in range(n):
    ox_list = list(input())
    score =0
    add_score = 0
    for i in ox_list:
        for ch in i:
            if ch =='O':
                add_score +=1 
                score = score + add_score
            elif ch=='X':
                add_score = 0

    print(score)