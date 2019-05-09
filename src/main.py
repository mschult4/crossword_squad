#import PySimpleGUI as sg      
import sys 
from jumble import jumble_solver
from cross import cross_solver
 
if sys.version_info[0] >= 3:  
    import PySimpleGUI as sg  
else:  
    import PySimpleGUI27 as sg  

layout = [[sg.Text('Type the Jumble Here:')],
          #[sg.Text('', key='_OUTPUT_') ],  
          [sg.Input(do_not_clear=False, key='_IN_')],  
          [sg.Button('UnJumble'), sg.Button('Exit')],
          [sg.Text('Type the Crossword Partial Answer Here (?ELLO):')],
          [sg.Input(do_not_clear=False, key='_CROSSIN_')],
          [sg.Button('Crossword'), sg.Button('Exit')]]  

window = sg.Window('Window Title', layout)  

while True:                 # Event Loop  
  event, values = window.Read()  
  print(event, values)
  if event is None or event == 'Exit':  
      break  
  if event == 'UnJumble':  
      # change the "output" element to be the value of "input" element  
      #window.Element('_OUTPUT_').Update(values['_IN_'])
      print('hiya', values['_IN_'])
      clue = values['_IN_']
      result = jumble_solver(clue)
      jumble_result = ', '.join(result).upper()
      window.Close()
      
      layout = [[sg.Text('Type the Jumble Here:')],
          [sg.Text(jumble_result, key='_OUTPUT_') ],  
          [sg.Input(do_not_clear=False, key='_IN_')],  
          [sg.Button('UnJumble'), sg.Button('Exit')],
          [sg.Text('Type the Crossword Partial Answer Here (?ELLO):')],
          [sg.Input(do_not_clear=False, key='_CROSSIN_')],
          [sg.Button('Crossword'), sg.Button('Exit')]] 

      window = sg.Window('Window Title', layout)

  if event == 'Crossword':
      print('in values', values['_CROSSIN_'])
      clue = values['_CROSSIN_']
      result = cross_solver(clue)
      cross_result = '\n'.join(result).upper()
      #print(cross_result)

      window.Close()
      layout = [[sg.Text('Type the Jumble Here:')],
          [sg.Input(do_not_clear=False, key='_IN_')],  
          [sg.Button('UnJumble'), sg.Button('Exit')],
          [sg.Text('Type the Crossword Partial Answer Here (?ELLO):')],
          [sg.Text(cross_result, key='_CROSSOUTPUT_')],
          [sg.Input(do_not_clear=False, key='_CROSSIN_')],
          [sg.Button('Crossword'), sg.Button('Exit')]] 

      window = sg.Window('Window Title', layout)

window.Close()

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