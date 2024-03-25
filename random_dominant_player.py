import musicpy
from random import randint, choice, shuffle

dominant_names_dict = {'D7no1': 'D7-1', 'D9b': 'D9>', 'D9no1': 'D9-1',
              'D9bno1': 'D9>-1', 'D6': 'D76-5', 'D6b': 'D76>-5'}
rev_dom_names_dict = {v: k for k, v in dominant_names_dict.items()}



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
    root='3'
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
    root='3'
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

def get_dominant_answer(data, answer):
    chord_type = dominant_names_dict.get(data['chordType'], data['chordType'])

    user_answer = f'{chord_type}/{data["chordRoot"]}'
    chord_type, root = answer.split('/')
    chord_type = rev_dom_names_dict.get(chord_type, chord_type)
    root = f'root{root}'

    print(answer, user_answer)

    correct = answer == user_answer
    return correct, chord_type, root 


if __name__ == '__main__':
    chord,answer=random_dominant()
    musicpy.play(chord, wait=True, bpm=60)
    user_answer=f"D{input('D')}"
    if user_answer == answer:
        print(f'Congratulations! That was {answer}.')
    else:
        print(f'Unfortunately that was {answer}. Better luck next time.')
