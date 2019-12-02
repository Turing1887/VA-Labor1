from tkinter import *
import audio
import CSVWriter

#Set Username
print("New User: ")
username = str(input())

#Initialize UserWriter Class
uw = CSVWriter.CSVWriter(username)
#First read of data
uw.readUserData()
uw.addUserData(username)

def submit():
    slider_value = w.get()
    pause = slider_value/1000
    uw.addUserData(pause)
    audio.playPreset(audio.presets, audio.step, pause)
    audio.step+=1
    if audio.finish == True:
        uw.writeUserData()
        end()

def play():
    slider_value = w.get()
    pause = slider_value/1000
    audio.playPreset(audio.presets, audio.step, pause)

root = Tk()
root.geometry("800x800")

def end():
    root.destroy()

playbutton = Button(root, text="PLAY", fg="black", command= lambda:play())
playbutton.pack()
w = Scale(root, from_=0, to=5000, length=500, label="Set Pause", showvalue=0, orient=HORIZONTAL)
w.pack()
submitbutton = Button(root, text="SUBMIT", fg="black", command= lambda:submit())
submitbutton.pack()
finishbutton = Button(root, text="FINISH", fg="black", command= lambda:uw.writeUserData())
finishbutton.pack()

root.mainloop()
