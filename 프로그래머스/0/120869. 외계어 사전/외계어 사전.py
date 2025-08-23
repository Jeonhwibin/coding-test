def solution(spell, dic):
    spell_set = set(spell)

    for i in dic:
        if spell_set == set(i) :
            return 1

    return 2
