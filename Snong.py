from distutils.command.sdist import sdist
from tkinter import CENTER
import PySimpleGUI as sg

font = ('Helvetica', 70, 'bold italic')
sg.theme('DarkTeal9')
sg.set_options(font=font)
colors = (sg.theme_background_color(), sg.theme_background_color())
#ändring
columns_elements = [
    [sg.Text("Welcome to our Game Hub!")],
    [sg.Text("Please select your game")],
    [sg.Button("Snake", key="snake", size=(25,1), pad=(0,30))],
    [sg.Text("Wins: " + str(7), font=('Helvetica', 20, 'bold italic'))],
    [sg.Button("Pong", key="pong", size=(25,1), pad=(0,30))],
    [sg.Text("Wins: " + str(7), font=('Helvetica', 20, 'bold italic'))],
    [sg.Button("Snong", key="snong", size=(25,1), pad=(0,30))],
    [sg.Text("Wins: " + str(7), font=('Helvetica', 20, 'bold italic'))],
]

layout = [[sg.Column(columns_elements,element_justification='center',justification='center')]]
        


window = sg.Window("Game Hub", layout, location=(0,0), size=(1440,800)).Finalize()
window.Maximize() 

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "snake":
        break
    if event == "pong":
        break
    if event == "snong":
        break    
        
window.close()
