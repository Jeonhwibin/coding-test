def solution(s, skip, index):
    skipped = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    res = ""
    for i in s:
        res += skipped[(skipped.index(i) + index) % len(skipped)]
    return res