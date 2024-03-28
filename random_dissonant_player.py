import musicpy
from random import randint, choice
import logging

CHORD_TYPES=['7','maj7','min7', 'minmaj7','maj6','min6', 'majmin6', 'minmaj6', '9no1','min9no1']
CHORD_MODES=['maj','maj','min','min','maj','min','maj', 'min', 'maj', 'maj']

def create_random_dissonant(root_note=None, chord_type=None):
    root_note= musicpy.degree_to_note(randint(48,72)) if root_note is None else root_note
    if root_note.name not in ['C', 'C#', 'D','Eb','E','F','F#', 'G', 'Ab', 'A', 'Bb','B']:
        root_note=~root_note
    chord_type=choice(CHORD_TYPES) if chord_type is None else chord_type
    if chord_type=='maj6':
        chord=musicpy.get_chord(root_note, '6')
    elif chord_type=='min6':
        chord=musicpy.get_chord(root_note-4, 'M7')/1
    elif chord_type=='majmin6':
        chord=musicpy.get_chord(root_note-4, 'M7b5')/1
    elif chord_type=='minmaj6':
        chord=musicpy.get_chord(root_note,'m6')
    elif chord_type=='minmaj7':
        chord=musicpy.get_chord(root_note, 'mM7')
    elif chord_type=='9no1':
        chord=musicpy.get_chord(root_note+4, 'half-dim')
    elif chord_type=='min9no1':
        chord=musicpy.get_chord(root_note+4, 'dim7')
    else:        
        chord=musicpy.get_chord(root_note, chord_type)
    if chord_type=='7':
        inversion=randint(0, 3)
        if inversion!=0:
            chord/=inversion
    answer=f'{root_note.name}{chord_type}'
    return chord, answer

def get_dissonant_answer(data, answer):
    logging.debug(data)
    root=data["chordRootName"]
    chord_mode=data["chordMode"]
    chord_type=data["chordType"]
    if (chord_mode is None or chord_mode=='maj') and chord_type not in ('maj6','min6'):
        user_answer=f'{root}{chord_type}'
    elif chord_mode=='maj' and chord_type=='maj6':
        user_answer=f'{root}{chord_type}'
    elif chord_mode=='min' and chord_type=='min6':
        user_answer=f'{root}{chord_type}'
    else:
        user_answer=f'{root}{chord_mode}{chord_type}'

    logging.debug(f'{answer =}, {user_answer =}')

    correct = answer == user_answer
    for ct in CHORD_TYPES:
        if ct in answer:
            chord_type=ct
    root=answer[:answer.index(chord_type)]
    chord_mode=CHORD_MODES[CHORD_TYPES.index(chord_type)]
    if chord_type=='min7':
        chord_type='7'
    if chord_type=='minmaj7':
        chord_type='maj7'
    if chord_type in ('minmaj6'):
        chord_type='maj6'
    if chord_type=='majmin6':
        chord_type='min6'
    return correct, root, chord_mode, chord_type 

if __name__ == '__main__':

    piece=None
    for i in range(6):
        chord, answer=create_random_dissonant()
        musicpy.play(chord, wait=True, bpm=60)
        user_answer=input('Chord: ')

        if user_answer == answer:
            print(f'Congratulations! That was {answer}.')
        else:
            print(f'Unfortunately that was {answer}. Better luck next time.')