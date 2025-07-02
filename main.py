from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = "kjlasfdjkbfsaouibo4bqu3gho78gh732uib48"
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app)