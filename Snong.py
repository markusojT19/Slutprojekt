from distutils.command.sdist import sdist
import PySimpleGUI as sg

layout = [
    [sg.Text("Welcome to our Game Hub!")],
    [sg.Text("Please select your game")],
    [sg.Button("Snake", key="snake")],
    [sg.Button("Pong", key="pong")],
    [sg.Button("Snong", key="snong")],
    
    
]

window = sg.Window("Game Hub", layout)

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
