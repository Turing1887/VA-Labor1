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
        'f': 100,
        'L': 60,
        'phi': 0,
        'length': 0.05,
    },
    1:
    {
        'f': 100,
        'L': 60,
        'phi': 0,
        'length': 0.1
    },
    2:
    {
        'f': 100,
        'L': 60,
        'phi': 0,
        'length': 0.2
    },
    3:
    {
        'f': 100,
        'L': 60,
        'phi': 0,
        'length': 0.3
    },
    4:
    {
        'f': 100,
        'L': 60,
        'phi': 0,
        'length': 0.4
    },
    5:
    {
        'f': 100,
        'L': 60,
        'phi': 0,
        'length': 0.5
    },
    6:
    {
        'f': 100,
        'L': 60,
        'phi': 0,
        'length': 0.6
    },
    7:
    {
        'f': 100,
        'L': 60,
        'phi': 0,
        'length': 0.7
    },
    8:
    {
        'f': 100,
        'L': 60,
        'phi': 0,
        'length': 0.8
    },
    9:
    {
        'f': 100,
        'L': 60,
        'phi': 0,
        'length': 0.9
    },
    10:
    {
        'f': 100,
        'L': 60,
        'phi': 0,
        'length': 1.0
    },
    11:
    {
        'f': 100,
        'L': 60,
        'phi': 0,
        'length': 1.5
    },
    12:
    {
        'f': 100,
        'L': 60,
        'phi': 0,
        'length': 2.0
    },
    13:
    {
        'f': 250,
        'L': 60,
        'phi': 0,
        'length': 0.05,
    },
    14:
    {
        'f': 250,
        'L': 60,
        'phi': 0,
        'length': 0.1
    },
    15:
    {
        'f': 250,
        'L': 60,
        'phi': 0,
        'length': 0.2
    },
    16:
    {
        'f': 250,
        'L': 60,
        'phi': 0,
        'length': 0.3
    },
    17:
    {
        'f': 250,
        'L': 60,
        'phi': 0,
        'length': 0.4
    },
    18:
    {
        'f': 250,
        'L': 60,
        'phi': 0,
        'length': 0.5
    },
    19:
    {
        'f': 250,
        'L': 60,
        'phi': 0,
        'length': 0.6
    },
    20:
    {
        'f': 250,
        'L': 60,
        'phi': 0,
        'length': 0.7
    },
    21:
    {
        'f': 250,
        'L': 60,
        'phi': 0,
        'length': 0.8
    },
    22:
    {
        'f': 250,
        'L': 60,
        'phi': 0,
        'length': 0.9
    },
    23:
    {
        'f': 250,
        'L': 60,
        'phi': 0,
        'length': 1.0
    },
    24:
    {
        'f': 250,
        'L': 60,
        'phi': 0,
        'length': 1.5
    },
    25:
    {
        'f': 250,
        'L': 60,
        'phi': 0,
        'length': 2.0
    },
    26:
    {
        'f': 500,
        'L': 60,
        'phi': 0,
        'length': 0.05,
    },
    27:
    {
        'f': 500,
        'L': 60,
        'phi': 0,
        'length': 0.1
    },
    28:
    {
        'f': 500,
        'L': 60,
        'phi': 0,
        'length': 0.2
    },
    29:
    {
        'f': 500,
        'L': 60,
        'phi': 0,
        'length': 0.3
    },
    30:
    {
        'f': 500,
        'L': 60,
        'phi': 0,
        'length': 0.4
    },
    31:
    {
        'f': 500,
        'L': 60,
        'phi': 0,
        'length': 0.5
    },
    32:
    {
        'f': 500,
        'L': 60,
        'phi': 0,
        'length': 0.6
    },
    33:
    {
        'f': 500,
        'L': 60,
        'phi': 0,
        'length': 0.7
    },
    34:
    {
        'f': 500,
        'L': 60,
        'phi': 0,
        'length': 0.8
    },
    35:
    {
        'f': 500,
        'L': 60,
        'phi': 0,
        'length': 0.9
    },
    36:
    {
        'f': 500,
        'L': 60,
        'phi': 0,
        'length': 1.0
    },
    37:
    {
        'f': 500,
        'L': 60,
        'phi': 0,
        'length': 1.5
    },
    38:
    {
        'f': 500,
        'L': 60,
        'phi': 0,
        'length': 2.0
    },
    39:
    {
        'f': 750,
        'L': 60,
        'phi': 0,
        'length': 0.05,
    },
    40:
    {
        'f': 750,
        'L': 60,
        'phi': 0,
        'length': 0.1
    },
    41:
    {
        'f': 750,
        'L': 60,
        'phi': 0,
        'length': 0.2
    },
    42:
    {
        'f': 750,
        'L': 60,
        'phi': 0,
        'length': 0.3
    },
    43:
    {
        'f': 750,
        'L': 60,
        'phi': 0,
        'length': 0.4
    },
    44:
    {
        'f': 750,
        'L': 60,
        'phi': 0,
        'length': 0.5
    },
    45:
    {
        'f': 750,
        'L': 60,
        'phi': 0,
        'length': 0.6
    },
    46:
    {
        'f': 750,
        'L': 60,
        'phi': 0,
        'length': 0.7
    },
    47:
    {
        'f': 750,
        'L': 60,
        'phi': 0,
        'length': 0.8
    },
    48:
    {
        'f': 750,
        'L': 60,
        'phi': 0,
        'length': 0.9
    },
    49:
    {
        'f': 750,
        'L': 60,
        'phi': 0,
        'length': 1.0
    },
    50:
    {
        'f': 750,
        'L': 60,
        'phi': 0,
        'length': 1.5
    },
    51:
    {
        'f': 750,
        'L': 60,
        'phi': 0,
        'length': 2.0
    },
    52:
    {
        'f': 1000,
        'L': 60,
        'phi': 0,
        'length': 0.05,
    },
    53:
    {
        'f': 1000,
        'L': 60,
        'phi': 0,
        'length': 0.1
    },
    54:
    {
        'f': 1000,
        'L': 60,
        'phi': 0,
        'length': 0.2
    },
    55:
    {
        'f': 1000,
        'L': 60,
        'phi': 0,
        'length': 0.3
    },
    56:
    {
        'f': 1000,
        'L': 60,
        'phi': 0,
        'length': 0.4
    },
    57:
    {
        'f': 1000,
        'L': 60,
        'phi': 0,
        'length': 0.5
    },
    58:
    {
        'f': 1000,
        'L': 60,
        'phi': 0,
        'length': 0.6
    },
    59:
    {
        'f': 1000,
        'L': 60,
        'phi': 0,
        'length': 0.7
    },
    60:
    {
        'f': 1000,
        'L': 60,
        'phi': 0,
        'length': 0.8
    },
    61:
    {
        'f': 1000,
        'L': 60,
        'phi': 0,
        'length': 0.9
    },
    62:
    {
        'f': 1000,
        'L': 60,
        'phi': 0,
        'length': 1.0
    },
    63:
    {
        'f': 1000,
        'L': 60,
        'phi': 0,
        'length': 1.5
    },
    64:
    {
        'f': 1000,
        'L': 60,
        'phi': 0,
        'length': 2.0
    },
}