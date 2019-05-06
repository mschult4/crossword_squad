from words import Words
import PySimpleGUI as sg

def jumble_solver(clue):
    clue = clue.lower()
    from words import Words
    w = Words()
    w.import_words()
    lengths = w.lengths
    matching_len_words = lengths[len(clue)]
    letters = dict()
    possible_words = list()
    possible = True
    for c in clue:
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1
    for word in matching_len_words:
        for c, val in letters.items():
            if val == word.count(c):
                possible = True
            else:
                possible = False
                break
        if possible:
            possible_words.append(word)

    print('inside', possible_words)
    return possible_words
