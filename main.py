# main.py

import sys
sys.path.append("C:\\Users\\onani\\Desktop\\gridSort")

import setup
import location
import aisle

import functions
import gui
import tkinter as tk

def main(aisleList):
    
    window = tk.Tk()
    app = gui.Gui(window, "GRID", "1280X1920")

    app.addLocations()
    
    window.mainloop()


    '''l01 = location.Location(1, 1, 9, 2, 5905)
    l02 = location.Location(0, 0, 4, 0, 5905)

    #print(l01 != l02)

    #print( repr(l01) )
    # print(l01)

    KA = aisle.Aisle(100)

    # print(aisleList)

    test = [int(digit) for digit in str(l01).split()]

    print(l02.prevLocation())
    
    #print( functions.readableFormat(test, aisleList, KA.rows))'''


if __name__ == "__main__":

    # Retrive grid info from setup func
    #
    gridInfo = setup.setup()

    # Pass grid info to main func
    #
    main(gridInfo)