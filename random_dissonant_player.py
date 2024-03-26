import musicpy
from random import randint, choice

CHORD_TYPES=['7','maj7','min7', 'minmaj7','maj6','min6', 'majmin6', 'minmaj6', '9no1','min9no1']

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
    print(data)
    user_answer=answer

    print(answer, user_answer)

    correct = answer == user_answer
    return correct#, chord_type, root 

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