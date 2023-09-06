import customtkinter
from tkinter import *
from playsound import playsound
from gtts import *
import os

customtkinter.set_appearance_mode("dark")

window = customtkinter.CTk()
window.geometry("420x340")
window.title("kaki atsume")
window.resizable(False, False)



def initial():
    insertTXT = entry.get()
    speak = gTTS(text=insertTXT, lang='ja')
    speakarchive = 'archivespeak.mp3'
    speak.save(speakarchive)
    playsound(speakarchive)

def clearEntry():
    entry.delete(0, END)
    os.remove('archivespeak.mp3')

# def closeWindow():
#     window.destroy()


#FONT
mainFont = customtkinter.CTkFont(family="Consolas", size=15,weight="bold", slant="italic")
secFont = customtkinter.CTkFont(family="Bodoni", size=12, weight="bold", slant="italic")


#FRAME
frame= customtkinter.CTkFrame(master=window, width=420, height=340, fg_color="#302452")
frame.pack()

#TEXT
labelOne = customtkinter.CTkLabel(master=frame, text="テキストを入力してください", font=mainFont)
labelOne.place(x=110, y=50)

gitTXT = customtkinter.CTkLabel(master=frame, text='github.com/salzani ', font=secFont)
gitTXT.place(x=280, y=315)


#ENTRY
entry = customtkinter.CTkEntry(master=frame, width=200, fg_color="black", border_color="white")
entry.place(x=110, y=100)   


#BUTTONS
but = customtkinter.CTkButton(master=frame, text="変換する",width=110, fg_color="black", border_width=2, command=initial)
but.place(x=155, y=160 )

clear = customtkinter.CTkButton(master=frame, text="クリーン",width=70, fg_color="black", border_width=2, command=clearEntry)
clear.place(x=175,y=200)

# quit = customtkinter.CTkButton(master=frame, text="✗", width=30, fg_color="black", border_width=2, command=closeWindow)
# quit.place(x=375, y=10)




#IMAGE
chopIMG = PhotoImage(file="zoro.png")
chopIMG = chopIMG.subsample(5,5)
chopLAB = Label(image = chopIMG, bg="#302452")
chopLAB.place(x=0, y=200)


window.mainloop()