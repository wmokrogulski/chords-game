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
    chord_type='7'
    chord=musicpy.get_chord(root_note,chord_type)
    chord-=chord[0]
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
    answer=f'D{chord_type}-1/{root}'
    return chord, answer

if __name__ == '__main__':
    chord, chord_type=create_dominant9()
    musicpy.play(chord, wait=True, bpm=60)
    answer=f'D{chord_type}'
    # user_answer=input('D7/')
    print(f'That was {answer}.')
    # if user_answer == root_note:
    #     print(f'Congratulations! That was {answer}.')
    # else:
    #     print(f'Unfortunately that was {answer}. Better luck next time.')
