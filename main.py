from Tkinter import *
import numpy as np
from scipy import signal
import simpleaudio as sa
import time

root = Tk()
logo = PhotoImage(file="../images/python_logo_small.gif")
w1 = Label(root, image=logo).pack(side="right")
explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface
exists to allow additional image file
formats to be added easily."""
w2 = Label(root,
           justify=LEFT,
           padx = 10,
           text=explanation).pack(side="left")
root.mainloop()

Fs = 44100                      #sampling rate
Ts = 1.0 / Fs                   #sampling interval
seconds = 2                     #sound duration
pauseSeconds = 0.5              #pause duration

presets = {
    'preset1':
    {
        'f': 1000,
        'L': 60,
        'phi': 0,
        'length': 0.1
    },
    'preset2':
    {
        'f': 1000,
        'L': 60,
        'phi': 0,
        'length': 0.2
    },
    'preset3':
    {
        'f': 1000,
        'L': 60,
        'phi': 0,
        'length': 0.4
    },
    'preset4':
    {
        'f': 1000,
        'L': 60,
        'phi': 0,
        'length': 0.75
    },
    'preset5':
    {
        'f': 1000,
        'L': 60,
        'phi': 0,
        'length': 1.0
    },
    'preset6':
    {
        'f': 300,
        'L': 60,
        'phi': 0,
        'length': 0.1
    },
    'preset6':
    {
        'f': 300,
        'L': 60,
        'phi': 0,
        'length': 0.2
    },
    'preset7':
    {
        'f': 300,
        'L': 60,
        'phi': 0,
        'length': 0.4
    },
    'preset8':
    {
        'f': 300,
        'L': 60,
        'phi': 0,
        'length': 0.75
    },
    'preset9':
    {
        'f': 300,
        'L': 60,
        'phi': 0,
        'length': 1.0
    },
    'preset10':
    {
        'f': 2000,
        'L': 60,
        'phi': 0,
        'length': 0.1
    },
    'preset11':
    {
        'f': 2000,
        'L': 60,
        'phi': 0,
        'length': 0.2
    },
    'preset12':
    {
        'f': 2000,
        'L': 60,
        'phi': 0,
        'length': 0.4
    },
    'preset13':
    {
        'f': 2000,
        'L': 60,
        'phi': 0,
        'length': 0.75
    },
    'preset14':
    {
        'f': 2000,
        'L': 60,
        'phi': 0,
        'length': 1.0
    },
    'preset15':
    {
        'f': 10000,
        'L': 60,
        'phi': 0,
        'length': 0.1
    },
    'preset16':
    {
        'f': 10000,
        'L': 60,
        'phi': 0,
        'length': 0.2
    },
    'preset17':
    {
        'f': 10000,
        'L': 60,
        'phi': 0,
        'length': 0.4
    },
    'preset18':
    {
        'f': 10000,
        'L': 60,
        'phi': 0,
        'length': 0.75
    },
    'preset19':
    {
        'f': 10000,
        'L': 60,
        'phi': 0,
        'length': 1.0
    }
}

def sinus(f=1000, L=60, phi=0, seconds=1):
    t = np.arange(0,seconds,Ts)     #time vector (start time, end time, number of entrys between)
    w = 2 * np.pi * f
    a = L * np.sin((w * t) + phi)
    return a

def playAudio(note):
    audio = note * (2**15 - 1) / np.max(np.abs(note))   # ensure that highest value is in 16-bit range
    audio = audio.astype(np.int16)                      #convert to 16-bit data

    play_obj = sa.play_buffer(audio, 1, 2, Fs)
    play_obj.wait_done()

def playPreset(preset)
    playAudio(sinus('f' in preset, 'L' in preset, 'phi' in preset, 'length' in preset))
