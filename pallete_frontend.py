from tkinter import *
from pallete_back import *

class ColorButton(Button):
    def __init__(self,master,posy,posx, *args, **kwargs):
        Button.__init__(self,master,*args,**kwargs)
        self.config(width = 10,height = 3,bd = 1, relief = SOLID)
        self.grid(row=posy,column=posx)

window=Tk()
window.geometry("300x400")
window.resizable(False,False)
window.title("Color Picker")

frame = Frame(window)

# BUTTON DECLARATION AND PLACEMENT
red = ColorButton(frame,0,1,text="RED", bg="red",command = lambda :change_red(window))
blue = ColorButton(frame,0,2,text="BLUE", bg="blue",command = lambda :change_blue(window))
yellow = ColorButton(frame,0,3,text="YELLOW", bg="yellow",command = lambda :change_yellow(window))
pink = ColorButton(frame,1,1,text="PINK", bg="pink",command = lambda : change_pink(window))
green = ColorButton(frame,1,2,text="GREEN", bg="green",command = lambda : change_green(window))
purple = ColorButton(frame,1,3,text="PURPLE", bg="purple",command = lambda : change_purple(window))
orange = ColorButton(frame,2,1,text="ORANAGE", bg="orange",command = lambda : change_orange(window))
silver = ColorButton(frame,2,2,text="SILVER", bg="silver",command = lambda : change_silver(window))
white = ColorButton(frame,2,3,text="WHITE", bg="white",command = lambda : change_white(window))
# BUTTON DECLARATION AND PLACEMENT

frame.place(in_=window, anchor="c", relx=.5, rely=.5)

window.mainloop()