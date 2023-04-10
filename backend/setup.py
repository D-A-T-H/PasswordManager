import PySimpleGUI as sg
import os

KeyboardInterrupt = True
sg.theme('DarkGrey8')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Push(), sg.Text('Welcome Dath Password locker', justification='c'), sg.Push()],
          
            [sg.Push(),sg.Text("Select files or folder:"), sg.Input(key='-IN1-',size=(40, 10),enable_events=True, readonly=True,background_color='#ffd22b',text_color='Black'),sg.FolderBrowse('Select', enable_events=True),sg.Push()],
            
            [sg.VPush()],
            [sg.Push(), sg.Button('Ok', disabled=True, key='okB',size=(20,5)), sg.Button('Cancel', size=(20,5)), sg.Push() ]]



# Create the Window
window = sg.Window('Dath Password Project', layout, icon="backend/dath_logo.ico", size= [750, 500])

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if os.path.exists(values['Select']):
        window['okB'].update(disabled=False)
    if event == 'okB':
        
        
        #Link all of the files that retain to the local locker  
        
        
        pass
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
window.close()
