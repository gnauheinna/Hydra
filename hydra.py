import tkinter
from tkinter import *
from tkinter import ttk

class myHydra:
    #initialize call (object) with values
    def __init__(self, name):
        self.name = name
    
    def popup():
        #create and confique window
        window = Tk()
        window.title("Hydra")
        window.geometry("500x300")

        def close_window():
            window.destroy()
        def disable_event():
            pass

        def spawn():
            # open two identival windows by creating instance of hydra object
            hydra_one = myHydra("twins")
            myHydra.popup()
            myHydra.popup()

        #fallsafe close button for window
        btn = ttk.Button(window, text = "FAIL SAFE CLOSE BTN", command=close_window);
        btn.pack();

        #change close button functionality by using protocol()
        window.protocol("WM_DELETE_WINDOW", spawn);
        window.mainloop();

#------------Initial Window--------
#create and confique window
window = Tk()
window.title("Hydra")
window.geometry("500x300")

def close_window():
    window.destroy()
def disable_event():
    pass

def spawn():
    # open two identival windows by creating instance of hydra object
    hydra_one = myHydra("twins")
    myHydra.popup()
    myHydra.popup()

#fallsafe close button for window
btn = ttk.Button(window, text = "FAIL SAFE CLOSE BTN", command=close_window);
btn.pack();

#change close button functionality by using protocol()
window.protocol("WM_DELETE_WINDOW", spawn);
window.mainloop();