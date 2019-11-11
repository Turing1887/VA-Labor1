from tkinter import *
import audio

def submit():
    slider_value = w.get()
    print(slider_value)
    pause = slider_value/1000-0.22
    audio.step+=1
    audio.playPreset(audio.presets, audio.step, )

def play():
    slider_value = w.get()
    print(slider_value)
    pause = slider_value/1000-0.22
    audio.setPause(slider_value/1000)
    audio.playPreset(audio.presets, audio.step, pause)
    
root = Tk()
root.geometry("800x800")


# mainframe = Frame(width=768, height=576, bg="", colormap="new")
# mainframe.pack()
#logo = PhotoImage(file="../images/python_logo_small.gif")
# w1 = Label(root, image=logo).pack(side="right")
# explanation = """At present, only GIF and PPM/PGM
# formats are supported, but an interface
# exists to allow additional image file
# formats to be added easily."""
# w2 = Label(root,
#            justify=LEFT,
#            padx = 10,
#            text=explanation).pack(side="left")
playbutton = Button(root, text="PLAY", fg="black", command= lambda:play())
playbutton.pack()
w = Scale(root, from_=0, to=5000, length=500, label="Set Pause", showvalue=0, orient=HORIZONTAL)
w.pack()
submitbutton = Button(root, text="SUBMIT", fg="black", command= lambda:submit())
submitbutton.pack()

root.mainloop()
