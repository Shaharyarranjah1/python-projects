import os
from tkinter import *

st =  Tk()
st.title("Shutdown app")
st.geometry("500x500")
st.config(bg="blue")


def restart():
   os.system("shutdown /r /t 1")
   
def restart_time():
   os.system("shutdown /r /t 20")
   
def logout():
   os.system("shutdown -1")
   
def shutdown():
   os.system("shutdown /s /t 1")


r_button = Button(st, text= "Restart", font=('Time New Roman', 30, "Bold"), relief=RAISED, cursor= "plus", command=restart)
r_button.place(x=150, y=60, height=40, width=200)


rt_button = Button(st, text= "Restart Time", font=('Time New Roman', 20, "Bold"), relief=RAISED, cursor= "plus", command=restart_time)
rt_button.place(x=150, y=170, height=50, width=200)


lg_button = Button(st, text= "Log Out", font=('Time New Roman', 30, "Bold"), relief=RAISED, cursor= "plus", command=logout)
lg_button.place(x=150, y=270, height=40, width=200)


st_button = Button(st, text= "Shut Down", font=('Time New Roman', 30, "Bold"), relief=RAISED, cursor= "plus", command=shutdown)
st_button.place(x=150, y=370, height=40, width=200)


st.mainloop()