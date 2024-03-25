from musicpy import *
from musicpy.daw import *
import base64
from random import choice


def export_sound(sound):
  filename = 'test.wav'

  new_song = daw(1, name='sound')
  new_song.load(0, 'MuseScore_General.sf3')

  new_song.export(sound, channel_num=0, mode='wav',
                  filename=filename)

  with open(filename, 'rb') as f:
      text = base64.b64encode(f.read())
  b64 = text.decode()
  audio_b64 = f'data:audio/wav;base64,{b64}'
  return audio_b64
