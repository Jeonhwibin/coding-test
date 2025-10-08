def solution(name, yearning, photo):
    c = dict(zip(name,yearning))
    answer =[]
    for i in photo:
        total = 0
    
        for j in i:
            if j in c.keys():
                total += c[j]
            else:
                continue
        
        answer.append(total)
    
    return answer