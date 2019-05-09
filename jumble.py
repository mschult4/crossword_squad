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

'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''