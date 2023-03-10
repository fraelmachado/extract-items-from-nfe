from PySimpleGUI import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color

left_col = [[sg.Text('Folder:'), sg.In(size=(25, 1), enable_events=True, key='-FOLDER-'), sg.FolderBrowse()]]
layout = [[sg.Column(left_col, element_justification='c')]]
window = sg.Window('Multiple Format Image Viewer', layout, resizable=True)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == '-FOLDER-':
        folder = values['-FOLDER-']


# # All the stuff inside your window.
# layout = [
#     [sg.Text('Some text on Row 1')],
#     [sg.Text('Enter something on Row 2'), sg.InputText()],
#     [sg.Button('Ok'), sg.Button('Cancel')]
# ]

# # Create the Window
# window = sg.Window('Window Title', layout)
# # Event Loop to process "events" and get the "values" of the inputs
# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
#         break
#     print('You entered ', values[0])

window.close()
