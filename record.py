from tkinter import *
from tkinter import messagebox
import time
from scipy.io.wavfile import write
import wavio as wv
import sounddevice as sound


root = Tk()
root.geometry("600x700+ 400+80")
root.resizable(False, False)
root.title("Voice Recorder")
root.configure(background="#4a4a4a")

def Record():
   freq = 44100
   dur = int(dur.get())
   recording= sound.rec(dur*freq, samplerate=freq, channels=2)
# timer 
   try:
      tem = int(duration.get())
   except:
      print("please enter the right value:")
      
      
   while tem>0:
      root.update()
      time.sleep(1)
      tem = 1
      0
   
   if(tem ==0):
      messagebox.showinfo("Time count down","Tim's up ")
   Label(text=f"{str(tem)}", font="arial, 40", width=4, background="#4a4a4a").place(x=240, y=590)

   
   sound.wait()
   write("record.wav", freq, recording)
   


# root icon
image_icon =PhotoImage(file="") 
root.iconphoto(False, image_icon)

# logo

photo = PhotoImage(file="")
my_image = Label(image=photo, background="#4a4a4a")
my_image.pack(padx=5, pady= 5)

# name label
Label(text="Voice recorder", font="arial 30 bold", background="#4a4a4a",fg="white").pack()


# entry box

duration = StringVar()
entry = Entry(root, textvariable=duration, font="arial 30", width=15).pack(pady=10)

# button

record = Button(root, font="arial 20", text="Record", bg="#111111",fg="white", border=0, ).pack(pady=30)








root.mainloop()