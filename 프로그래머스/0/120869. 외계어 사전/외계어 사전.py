def solution(spell, dic):
    spell_sorted=sorted(spell)
    for letter in dic:
        letter_sorted=sorted(letter)
        if letter_sorted==spell_sorted:
            return 1
    return 2
                