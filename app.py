from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clavesecreta'
app.config['JSON_SORT_KEYS'] = False
socketio = SocketIO(app)


@app.route('/', methods=['GET'])
def root_route():
    #handleMessage("Bienvenidos !!")
    return render_template('index.html')

@socketio.on('message')
def handleMessage(msg):
    print("Message: " + msg)
    send(msg, broadcast = True)

if __name__ == '__main__':
    socketio.run(app, debug = True)
