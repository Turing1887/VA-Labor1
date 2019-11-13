import numpy as np
from scipy import signal
import simpleaudio as sa
import time

Fs = 44100                      #sampling rate
Ts = 1.0 / Fs                   #sampling interval
seconds = 2                     #sound duration
pauseSeconds = 0.5              #pause duration
step = 0
repetition = 10

def setPause(newPause):
  pauseSeconds = newPause

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

def playPreset(presets, step, pause):
  sound = []
  if pause < 0:
    pause = 0
  sin = sinus(presets[step]['f'], presets[step]['L'], presets[step]['phi'], presets[step]['length'])
  pause = np.zeros(np.ceil(pause * Fs).astype(int))
  for x in range(repetition):
    sound = appendSounds(sound, sin)
    sound = appendSounds(sound, pause)
  playAudio(sound)

def appendSounds(baseSignal, addSignal):
  return np.append(baseSignal, addSignal, axis=0)

presets = {
    0:
    {
        'f': 1000,
        'L': 60,
        'phi': 0,
        'length': 0.1,
    },
    1:
    {
        'f': 1000,
        'L': 60,
        'phi': 0,
        'length': 0.2
    },
    2:
    {
        'f': 1000,
        'L': 60,
        'phi': 0,
        'length': 0.4
    },
    3:
    {
        'f': 1000,
        'L': 60,
        'phi': 0,
        'length': 0.75
    },
    4:
    {
        'f': 1000,
        'L': 60,
        'phi': 0,
        'length': 1.0
    },
    5:
    {
        'f': 300,
        'L': 60,
        'phi': 0,
        'length': 0.1
    },
    6:
    {
        'f': 300,
        'L': 60,
        'phi': 0,
        'length': 0.2
    },
    7:
    {
        'f': 300,
        'L': 60,
        'phi': 0,
        'length': 0.4
    },
    8:
    {
        'f': 300,
        'L': 60,
        'phi': 0,
        'length': 0.75
    },
    9:
    {
        'f': 300,
        'L': 60,
        'phi': 0,
        'length': 1.0
    },
    10:
    {
        'f': 2000,
        'L': 60,
        'phi': 0,
        'length': 0.1
    },
    11:
    {
        'f': 2000,
        'L': 60,
        'phi': 0,
        'length': 0.2
    },
    12:
    {
        'f': 2000,
        'L': 60,
        'phi': 0,
        'length': 0.4
    },
    13:
    {
        'f': 2000,
        'L': 60,
        'phi': 0,
        'length': 0.75
    },
    14:
    {
        'f': 2000,
        'L': 60,
        'phi': 0,
        'length': 1.0
    },
    15:
    {
        'f': 10000,
        'L': 60,
        'phi': 0,
        'length': 0.1
    },
    16:
    {
        'f': 10000,
        'L': 60,
        'phi': 0,
        'length': 0.2
    },
    17:
    {
        'f': 10000,
        'L': 60,
        'phi': 0,
        'length': 0.4
    },
    18:
    {
        'f': 10000,
        'L': 60,
        'phi': 0,
        'length': 0.75
    },
    19:
    {
        'f': 10000,
        'L': 60,
        'phi': 0,
        'length': 1.0
    }
}