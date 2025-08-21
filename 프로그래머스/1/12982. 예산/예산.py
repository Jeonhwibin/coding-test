def solution(d, budget):
    total = 0
    sorted_d =sorted(d)
    answer = 0
    for i in sorted_d:
        total += i
        if total <= budget:
            answer += 1

    return answer