from words import Words


def jumble_solver():
    w = Words()
    w.import_words()
    lengths = w.lengths
    clue = input("Enter clue: ")
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

    return possible_words


def main():
    print(jumble_solver())


if __name__ == "__main__":
    main()
