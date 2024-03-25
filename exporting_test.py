from musicpy import *
from musicpy.daw import *
import base64
from random import choice

filename = 'test.wav'

new_song = daw(1, name='my first song')
new_song.load(0, 'MuseScore_General.sf3')

chord_structures = {
    'major': [
        ', ++4, ++3',
        ', ++3, ++5',
        ', ++5, ++4'
    ],
    'minor': [
        ', ++3, ++4',
        ', ++4, ++5',
        ', ++3, ++4'
    ]
}

chord_types = list(chord_structures.keys())
notes = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']
octaves = ['2', '3', '4', '5']

chord = chord(
    f"{choice(notes)}{choice(octaves)}{choice(chord_structures[choice(chord_types)])}"
)
play(chord, wait=True)
# chord = get_chord(
#     f"{choice(notes)}{choice(octaves)}",
#     interval=choice(chord_structures[choice(chord_types)])
# )
# piece = P(C('D'), C('E'))

new_song.export(chord, channel_num=0, mode='wav',
                filename=filename)

with open(filename, 'rb') as f:
    text = base64.b64encode(f.read())
# os.remove(filename)
b64 = text.decode()
audio = f'<audio autoplay controls src = "data:audio/wav;base64,{b64}" > The audio tag is not supported by your browser.</audio >'
with open('test.txt', 'w') as f:
    f.write(audio)
