def solution(lottos, win_nums):
    zero_cnt = lottos.count(0)
    correct_cnt = len(set(lottos) & set(win_nums))

    def rank(n):
        return 6 if n < 2 else 7 - n

    return [rank(correct_cnt + zero_cnt), rank(correct_cnt)]