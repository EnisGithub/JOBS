from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
import time
from threading import Thread

app = Flask(__name__)
socketio = SocketIO(app)

# Logs an die Website senden
def log_to_website(message):
    print(message)  # Ausgabe in die normale Konsole
    socketio.emit("console_log", {"message": message})  # An die Website senden

# Beispiel-Funktion, die ausgeführt wird
def run_python_script():
    log_to_website("Python-Skript gestartet...")
    time.sleep(2)
    log_to_website("Skript läuft...")
    time.sleep(2)
    log_to_website("Skript beendet!")

# Route für die Startseite
@app.route("/")
def index():
    return render_template("index.html")

# API-Route, um das Python-Skript auszuführen
@app.route("/run-script", methods=["POST"])
def run_script():
    Thread(target=run_python_script).start()  # Skript in einem eigenen Thread ausführen
    return jsonify({"message": "Skript gestartet!"})

# Hauptprogramm
if __name__ == "__main__":
    print("Server läuft...")
    socketio.run(app, host="0.0.0.0", port=8080)
