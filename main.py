from flask import Flask, render_template
from flask_socketio import SocketIO
from random_dominant_player import random_dominant, get_dominant_answer
import musicpy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
answer = None
chord = None
game = None




@app.route("/dominants/")
def dominants():
    global game
    game='dominants'
    return render_template("dominants.html")


@socketio.on('play')
def handle_play():
    global answer
    global chord
    if answer is None:
        if game=='dominants':
            chord, answer = random_dominant()
    musicpy.play(chord, wait=True, bpm=60)


@socketio.on('next')
def handle_next():
    global answer
    answer = None


@socketio.on('answer')
def handle_answer(data):
    global game
    global answer
    if game=='dominants':
        correct, chord_type, root = get_dominant_answer(data, answer)
        socketio.emit('answer_returned', {
                    'correct': correct, 'chord_type': chord_type, 'chord_root': root})


if __name__ == '__main__':
    socketio.run(app)
