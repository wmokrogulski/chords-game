from flask import Flask, render_template
from flask_socketio import SocketIO
from random_dominant_player import random_dominant, get_dominant_answer
from random_dissonant_player import create_random_dissonant, get_dissonant_answer
from sound_exporter import export_sound
import musicpy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")
answer = None
chord = None
game = None

MAX_TRIES=3
DEFAULT_TOTAL=10

tries = 0
total = DEFAULT_TOTAL
current = 0
points = 0



@app.route("/dominants/")
def dominants():
    global game
    game='dominants'
    return render_template("dominants.html")

@app.route("/dissonant/")
def dissonant():
    global game
    global current
    global points
    global tries
    current=1
    points=0
    tries=0
    game='dissonant'
    return render_template("dissonant.html")

@socketio.on('play')
def handle_play():
    global answer
    global chord
    if answer is None:
        if game=='dominants':
            chord, answer = random_dominant()
        if game == 'dissonant':
            chord, answer = create_random_dissonant()
    print(f'{answer = }')
    audio_b64=export_sound(chord)
    socketio.emit('play_returned',{'audio_b64':audio_b64})


@socketio.on('next')
def handle_next():
    global answer
    global current
    global tries
    answer = None
    current += 1
    tries = 0


@socketio.on('answer')
def handle_answer(data):
    global game
    global answer
    global tries
    global points
    if game=='dominants':
        correct, chord_type, root = get_dominant_answer(data, answer)
        if correct:
            points+=1
        else:
            tries+=1
        socketio.emit('answer_returned', {
                    'correct': correct, 'chord_type': chord_type, 'chord_root': root})
    if game=='dissonant':
        correct, root, chord_mode, chord_type = get_dissonant_answer(data, answer)
        if correct:
            if tries==0:
                points+=1
            else:
                points+=0.5
        else:
            tries+=1
        socketio.emit('answer_returned', {'correct': correct, 'tries': tries,  'chord_root': root, 'chord_mode':chord_mode,'chord_type': chord_type})


if __name__ == '__main__':
    socketio.run(app)
