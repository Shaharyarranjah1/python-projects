from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob



def label_change():
   c = combo1.get()
   c1 = combo2.get()
   label1.configure(text=c)
   label2.configure(text=c1)
   root.after(1000, label_change)

def translate_now():
   global language
   try:
      text_=text1.get(1.0, END)
      c2 = combo1.get()
      c3= combo2.get()
      if(text_):
         words = textblob.TextBlob(text_)
         lan = words.detect_language()
         for i,j in language.items():
            if(j==c3):
               lan_ = i
      
         words = words.translate(from_lang=lan, to=str(lan_))
         text2.delete(1.0, END)
         text2.insert(END, words)
   except Exception as e:
      messagebox.showerror("googletrans", "please try again later")

root = Tk()
root.title("Google Translater")
root.geometry("1080x 800")

# icon
image_icon = PhotoImage(file="")
root.iconphoto(False, image_icon)

# arrow image
arrow_image = PhotoImage(file="")
image_label = Label(root, image = arrow_image, width=150)
image_label.place(x=460, y=50)


language  = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()



combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state='r')
combo1.place(x=110, y=20)
combo1.set("English")

label1 = Label(root, text="English", font="segoe 30, bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

f= Frame(root, bg='black', bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="Roboto, 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scorllbar1 = Scrollbar(f)
scorllbar1.pack(side="right", fill='y')
scorllbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scorllbar1.set)

combo2 = ttk.Combobox(root, values=languageV, font="Roboto, 14", state='r')
combo2.place(x=730, y=20)
combo2.set("Select Language")

label2 = Label(root, text="English", font="segoe, 30, bold", bg='white', width=18,bd=5, relief=GROOVE)
label2.place(x=620, y=50)

f1= Frame(root, bg='black', bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font="Roboto, 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scorllbar2 = Scrollbar(f1)
scorllbar2.pack(side="right", fill='y')
scorllbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scorllbar2.set)

# translate button
translate = Button(root, text="translate", font="Roboto 15 bold itaclic", activebackground='purple', cursor="hand2",bd=5, bg='red', fg='white', command=translate_now )
translate.place(x=480, y=250)

label_change()
root.config(bg="white")
root.mainloop()
