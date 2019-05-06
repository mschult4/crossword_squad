#import PySimpleGUI as sg      
import sys 
from jumble import jumble_solver
 
if sys.version_info[0] >= 3:  
    import PySimpleGUI as sg  
else:  
    import PySimpleGUI27 as sg  

layout = [[sg.Text('Type the Jumble Here:')],
          #[sg.Text('', key='_OUTPUT_') ],  
          [sg.Input(do_not_clear=False, key='_IN_')],  
          [sg.Button('Show'), sg.Button('Exit')]]  

window = sg.Window('Window Title', layout)  

while True:                 # Event Loop  
  event, values = window.Read()  
  print(event, values)
  if event is None or event == 'Exit':  
      break  
  if event == 'Show':  
      # change the "output" element to be the value of "input" element  
      #window.Element('_OUTPUT_').Update(values['_IN_'])
      print('hiya', values['_IN_'])
      clue = values['_IN_']
      result = jumble_solver(clue)
      jumble_result = ', '.join(result)
      #window.Element('_OUTPUT_').Update(size = (len(jumble_result), 1))
      #window.Element('_OUTPUT_').Update(jumble_result)
      window.Close()
      #print(layout)
      #layout.append(sg.Text(jumble_result, key='_OUTPUT_'))
      #print(layout)

      layout = [[sg.Text('Type the Jumble Here:')],
          [sg.Text(jumble_result, key='_OUTPUT_') ],  
          [sg.Input(do_not_clear=False, key='_IN_')],  
          [sg.Button('Show'), sg.Button('Exit')]]  
      window = sg.Window('Window Title', layout)
      

window.Close()
