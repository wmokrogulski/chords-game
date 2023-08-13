import musicpy
from random import randint, choice



def create_random_chord():
    root_note=musicpy.degree_to_note(randint(48,72))
    chord_type=choice(['maj','min','dim','aug','maj7','min7','7'])
    inversion=randint(0,0 if chord_type=='aug' else 3 if '7' in chord_type else 2)
    chord=musicpy.get_chord(root_note, chord_type)
    if inversion!=0:
        chord/=inversion
    return chord, root_note.base_name, chord_type, chord[0].base_name

if __name__ == '__main__':
    
    # print(chord.root)
    # chord.play(wait=True)
    piece=None
    for i in range(4):
        chord, root_note, chort_type, bass=create_random_chord()
        if bass==root_note:
          print(f"{root_note}{chort_type}")
        else:
          print(f"{root_note}{chort_type}/{bass}")
        if piece is None:
            piece=chord
        else:
            piece|=chord

    musicpy.play(piece, wait=True, bpm=60)