from words import Words
#import PySimpleGUI as sgi
import sys

def cross_solver(clue):
	clue = clue.lower().strip('\n')
	#print(clue)
	w = Words()
	w.import_words()
	lengths = w.lengths
	matching_len_words = lengths[len(clue)]
	letters = dict()
	possible_words = list()
	possible = True

	given_letter_pos = []
	last_pos = 0
	for index, letter in enumerate(clue):
		if letter is not '?':
			given_letter_pos.append(index)
			last_pos = index

	#print(given_letter_pos)

	matching_words = []
	for word in matching_len_words:
		for pos in given_letter_pos:
			if word[pos] != clue[pos]:
				break
			elif (word[pos] == clue[pos]) and pos == last_pos:
				matching_words.append(word)

	return matching_words

def main():
	while True:
		clue = input("Enter clue: ")
		print(cross_solver(clue))

if __name__ == "__main__":
	main()
