# Description: This program is a Tic Tac Toe game that uses the Minimax algorithm to play against the user.
import PySimpleGUI as sg
import sys as sistema
# from tkinter import *
# from tkinter import messagebox
from Stuff import *
sg.theme('DarkAmber') 
width = 15
buttonWidth = 10
height = 50
layout = [  [sg.Text('Welcome to Tic Tac Toe. '), sg.Text("Press in your play: ")],
            [sg.Button(" ",size=(width,width),key="0"), sg.Button(" ",size=(width,width),key="1"), sg.Button(" ",size=(width,width),key="2")],
            [sg.Button(" ",size=(width,width),key="3"), sg.Button(" ",size=(width,width),key="4"), sg.Button(" ",size=(width,width),key="5")],
            [sg.Button(" ",size=(width,width),key="6"), sg.Button(" ",size=(width,width),key="7"), sg.Button(" ",size=(width,width),key="8")]]

def main():
    window = sg.Window("Tic Tac Toe", layout)
    while True:
        
        event,values = window.read()
        # print(window.AllKeysDict)
        if sg.WINDOW_CLOSED == event:
            exit()
        if "0" in event:
            window[event].update("X")
        # if event == "0":
        #     pass
            # window[int(event)].update("X")
        actualBoard = Game()
        
        # teste(actualBoard) #Tests if the evaluation process is working properly
        
        while not Terminal(actualBoard.gameBoard):
            # actualBoard.show()
            play = int(event[0])
            if actualBoard.IsValid(int(play)):
                actualBoard.Assing(int(play))
                # actualBoard.show()
                board = actualBoard.gameBoard[:]
                InitNode = NodeGame(board)
                if actualBoard.Evaluate(actualBoard.Value()) == 0:
                    Minimax(InitNode, True)
                    best = 0
                    index = 0
                    counter = 0
                    for children in InitNode.children:
                        
                        if children.getValue() >= best:
                            best = children.getValue()
                            counter = index
                        index +=1
                            
                    actualBoard.gameBoard = InitNode.children[counter].gameBoard
                    caller = 0
                    for cells in actualBoard.gameBoard:
                        window[str(caller)].update(cells)
                        caller+=1
            else:
                print("Invalid position")
            # print("///////////////////////////////////////")
        # actualBoard.show()
        print("Game Over")
  
if __name__ == "__main__":
    main()
