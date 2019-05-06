from collections import defaultdict

class Words(object):
    def __init__(self):
        self.words_list = list()
        self.lengths = defaultdict(list)

    def import_words(self):
        for line in open('/usr/share/dict/words'):
            word = line.rstrip('\n')
            self.words_list.append(word)
            l = len(word)
            self.lengths[l].append(word)
