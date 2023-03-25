from tkinter import *
from tkinter import ttk
from googletrans import Translater, LANGUAGES

root=Tk()
root.title("Translater")
root.geometry("1080x400")
root.config(bg="white")

languages =list(LANGUAGES.value())
title_label = Label(root,text="LANGUAGES TRANSLATER", bg="white",font=("Sylfan",18,"bold","italic"))
title_label.place(relx=0.5,rely=0.1,anchor=CENTER)

title_label = Label(root,text="Enter Text", bg="white",font=("Sylfan",13,"bold"))
title_label.place(relx=0.2,rely=0.2,anchor=CENTER)
sl=ttk.Combobox(root,values=language,width=77,state="readonly")
sl.place(relx=0.13,rely=0.2,anchor=W)
sl.set('english')

title_label = Label(root,text="Output", bg="white",font=("Sylfan",13,"bold"))
title_label.place(relx=0.81,rely=0.2,anchor=CENTER)
dl=ttk.Combobox(root,values=language,width=22,state="readonly")
dl.place(relx=0.98,rely=0.2,anchor=E)
dl.set('choose output languages')

i= Test(root,text="Output", bg="white",font=("Sylfan",10,"bold"),wrap=WORD,height=11,width=60,padx=5,pady=5,bd=0)
i.place(relx=0.81,rely=0.2,anchor=E)
o= Test(root,text="Output", bg="white",font=("Sylfan",10,"bold"),wrap=WORD,height=11,width=60,padx=5,pady=5,bd=0)
o.place(relx=0.81,rely=0.2,anchor=E)

def translate():
    translater=Translator()
    try:
        translated=translator.translate(text=i.get(1.0,END),src=sl.get(),dl=dl.get())
        o.delete(1.0,END)
        o.insert(END,translated.text)
    except:
        print("Try again")
        
btn=Button(root, text='translate',font='arial 12 bold',pady=5,command=translate,bg="white",activebackground="black")
btn.place(relx=0.5,rely=0.85,anchor=CENTER)

root.mainloop()