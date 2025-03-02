import pyautogui 
from tkinter import *

def take_ss():
   add_data = entry.get()
   path = add_data+"\\test.png"
   ss = pyautogui.screenshot()
   ss.save(path)


   

window = Tk()
window.title("wsCube tech ss")
window.geometry("700x400")
window.config(bg= "yellow")
window.resizable(False, False)


entry = Entry(window, font=('time New Roman', 30))
entry.place(x=20, height=50, width=660, y=30)

# make the button 

button = Button(window, text="Done", font=("time New Roman", 50 ,), command=take_ss)
button.place(x=250, y=100, height=100, width=200)


window.mainloop()