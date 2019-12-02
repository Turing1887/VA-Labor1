import numpy as np
from scipy import signal
import simpleaudio as sa
import time
import CSVWriter

Fs = 44100                      #sampling rate
Ts = 1.0 / Fs                   #sampling interval
seconds = 2                     #sound duration
pauseSeconds = 0.5              #pause duration
step = 0
repetition = 10
finish = False

def sinus(f=1000, seconds=1):
  t = np.arange(0,seconds,Ts)     #time vector (start time, end time, number of entrys between)
  w = 2 * np.pi * f
  a = np.sin(w * t)
  return a

def playAudio(note):
  audio = note * (2**15 - 1) / np.max(np.abs(note))   # ensure that highest value is in 16-bit range
  audio = audio.astype(np.int16)                      #convert to 16-bit data

  play_obj = sa.play_buffer(audio, 1, 2, Fs)
  play_obj.wait_done()

def playPreset(presets, step, pause):
  sound = []
  if pause < 0:
    pause = 0
  sin = sinus(presets[step]['f'], presets[step]['length'])
  pause = np.zeros(np.ceil(pause * Fs).astype(int))
  for x in range(repetition):
    sound = appendSounds(sound, sin)
    sound = appendSounds(sound, pause)
  playAudio(sound)
  if step >= len(presets)-1:
    global finish
    finish = True
    return

def appendSounds(baseSignal, addSignal):
  return np.append(baseSignal, addSignal, axis=0)

presets = {
    0:
    {
        'f': 200,
        'length': 0.01,
    },
    1:
    {
        'f': 200,
        'length': 0.02
    },
    2:
    {
        'f': 200,
        'length': 0.05
    },
    3:
    {
        'f': 200,
        'length': 0.1
    },
    4:
    {
        'f': 200,
        'length': 0.2
    },
    5:
    {
        'f': 200,
        'length': 0.5
    },
    6:
    {
        'f': 200,
        'length': 1.0
    },
    7:
    {
        'f': 3200,
        'length': 0.01,
    },
    8:
    {
        'f': 3200,
        'length': 0.02
    },
    9:
    {
        'f': 3200,
        'length': 0.05
    },
    10:
    {
        'f': 3200,
        'length': 0.1
    },
    11:
    {
        'f': 3200,
        'length': 0.2
    },
    12:
    {
        'f': 3200,
        'length': 0.5
    },
    13:
    {
        'f': 3200,
        'length': 1.0
    },
}
