import musicpy
from random import randint, choice



def create_random_dissonant():
    # root_note=musicpy.degree_to_note(randint(48,72))
    root_note=musicpy.N('C4')
    chord_type=choice(['7','maj7','min7', 'minmaj7','maj6','min6'])
    if chord_type=='maj6':
        chord=musicpy.chord(f'{root_note},++4,++3,++2')
    elif chord_type=='min6':
        chord=musicpy.chord(f'{root_note},++3,++4,++1')
    elif chord_type=='minmaj7':
        chord=musicpy.chord(f'{root_note},++3,++4,++4')
    else:        
        chord=musicpy.get_chord(root_note, chord_type)
    if chord_type=='7':
        inversion=randint(0, 3)
        if inversion!=0:
            chord/=inversion
    return chord, root_note.name, chord_type, chord[0].name

if __name__ == '__main__':

    piece=None
    for i in range(4):
        chord, root_note, chort_type, bass=create_random_dissonant()
        print(chord)
        if bass==root_note:
          print(f"{root_note}{chort_type}")
        else:
          print(f"{root_note}{chort_type}/{bass}")
        if piece is None:
            piece=chord
        else:
            piece|=chord

    musicpy.play(piece, wait=True, bpm=40)