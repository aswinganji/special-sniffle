from tkinter import*
import speech_recognition as sr

root = Tk()
root.geometry("500x500")

label1 = Label(root,text = "Plangage")
label2 = Label(root)

input1 = Entry(root)
label1.pack()
label2.pack()
input1.pack()


root.mainloop()