from tkinter import *
import customtkinter
import pyttsx3 

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title("Text to speech")
root.geometry("800x500")


engine = pyttsx3.init()
engine.setProperty("rate",125)

def talk():
    engine.say(my_entry.get())
    engine.runAndWait()
    my_entry.delete(0, END)




my_entry = customtkinter.CTkEntry(root, font=("Agency FB", 28))
my_entry.pack(pady=20)

my_button = customtkinter.CTkButton(root, text="Speak", command=talk, font=("Agency FB", 24))
my_button.pack(pady=20)





root.mainloop()