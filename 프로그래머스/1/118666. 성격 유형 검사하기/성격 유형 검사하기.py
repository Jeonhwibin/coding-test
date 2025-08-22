def solution(survey,choices):
    mbti = []
    # element = ["R","T","F","C","M","J","A","N"] 
    # ele_score=[0,0,0,0,0,0,0,0]
    element = {"R":0,"T":0,"F":0,"C":0,"M":0,"J":0,"A":0,"N":0}
    answer =''
    for i in range(len(choices)):
        if choices[i] >= 5:
            element[survey[i][1]] += choices[i] - 4
        elif choices[i] == 4:
            continue
        else:
            element[survey[i][0]] += 4 - choices[i]

    # if element["R"] >= element['T']:
    #     mbti.append["R"]
    #     answer = " ".join(mbti)
    # else:
    #     mbti.append["T"]
    #     answer = " ".join(mbti)
    if element["R"] >= element["T"]:
        answer += "R"
    else:
        answer += "T"

    if element["F"] > element["C"]:
        answer += "F"
    else:
        answer += "C"    
    
    if element["M"] > element["J"]:
        answer += "M"
    else:
        answer += "J"

    if element["A"] >= element["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer