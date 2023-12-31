import musicpy
from random import randint, choice, shuffle



def create_dominant7():
    root_note=musicpy.degree_to_note(randint(48,72))
    chord_type='7'
    inversion=randint(0,3)
    chord=musicpy.get_chord(root_note, chord_type)
    if inversion!=0:
        chord/=inversion
    root=(1,3,5,7)[inversion]
    answer=f'D7/{root}'
    return chord, answer

def create_dominant9():
    root_note=musicpy.degree_to_note(randint(48,67))
    chord_type='7'
    chord=musicpy.get_chord(root_note,chord_type)
    chord-=chord[2]
    chord_type=choice(('9>','9'))
    chord+=chord[2]+(3 if chord_type=='b9' else 4)
    root=choice((1,3,7))
    if root==1:
      rest=[2,3,4]
      shuffle(rest)
      chord=chord.sort([1]+rest)
      if rest[0]==4:
          chord[0]-=12
    elif root==3:
        chord=chord.sort([2,1,3,4])
    elif root==7:
        chord=chord.sort([3,1,2,4])
    answer=f'D{chord_type}/{root}'
    return chord, answer

def create_dominant9omit1():
    root_note=musicpy.degree_to_note(randint(48,67))
    chord_type=choice(('dim7','m7b5'))
    chord=musicpy.get_chord(root_note,chord_type)
    notes=[1,2,3,4]
    shuffle(notes)
    chord.sort(notes)
    root=str((1,3,5,7,9)[notes[0]])
    if chord_type=='dim7':
        chord_type='9>'
        if root=='9':
            root='9>'
    else:
        chord_type='9'
    
    answer=f'D{chord_type}-1/{root}'
    return chord, answer

def create_dominant7omit1():
    root_note=musicpy.degree_to_note(randint(48,67))
    chord_type='dim'
    chord=musicpy.get_chord(root_note,chord_type)
    notes=[1,2,3]
    shuffle(notes)
    chord.sort(notes)
    root=str((1,3,5,7)[notes[0]])
    chord_type='7'
    
    answer=f'D{chord_type}-1/{root}'
    return chord, answer

def create_chopin_chord():
    root_note=musicpy.degree_to_note(randint(48,67))
    chord=root_note+(root_note+10)+(root_note+16)
    root='1'
    chord_type=choice(('6','6>'))
    if chord_type=='6':
        chord+=root_note+21
    else:
        chord+=root_note+20
    
    answer=f'D7{chord_type}-5/{root}'
    return chord, answer

def random_dominant():
  chord, answer=choice((
      create_dominant7(),
      create_dominant9(),
      create_dominant9omit1(),
      create_dominant7omit1(),
      create_chopin_chord(),
  ))
  return chord,answer


if __name__ == '__main__':
    chord,answer=random_dominant()
    musicpy.play(chord, wait=True, bpm=60)
    user_answer=f"D{input('D')}"
    if user_answer == answer:
        print(f'Congratulations! That was {answer}.')
    else:
        print(f'Unfortunately that was {answer}. Better luck next time.')
