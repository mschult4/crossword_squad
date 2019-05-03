from words import Words


def jumble_solver():
    w = Words()
    w.import_words()
    words = w.words_list
    lengths = w.lengths


def main():
    jumble_solver()


if __name__ == "__main__":
    main()
