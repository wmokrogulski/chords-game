from flask import Flask, render_template
from flask_socketio import SocketIO
from random_dominant_player import random_dominant
import musicpy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
answer = None
chord = None

names_dict = {'D7no1': 'D7-1', 'D9b': 'D9>', 'D9no1': 'D9-1',
              'D9bno1': 'D9>-1', 'D6': 'D76-5', 'D6b': 'D76>-5'}
rev_names_dict = {v: k for k, v in names_dict.items()}


@app.route("/dominants/")
def hello_world():
    return render_template("dominants.html")


@socketio.on('play')
def handle_play():
    global answer
    global chord
    if answer is None:
        chord, answer = random_dominant()
    musicpy.play(chord, wait=True, bpm=60)


@socketio.on('next')
def handle_play():
    global answer
    answer = None


@socketio.on('answer')
def handle_answer(data):
    global names_dict
    global rev_names_dict
    chord_type = names_dict.get(data['chordType'], data['chordType'])

    user_answer = f'{chord_type}/{data["chordRoot"]}'
    chord_type, root = answer.split('/')
    chord_type = rev_names_dict.get(chord_type, chord_type)
    root = f'root{root}'

    print(answer, user_answer)

    correct = answer == user_answer

    socketio.emit('answer_returned', {
                  'correct': correct, 'chord_type': chord_type, 'chord_root': root})


if __name__ == '__main__':
    socketio.run(app)
