from flask import Flask, request, jsonify, send_from_directory
from app.mqtt_client import mqtt, send_settings, send_command, get_status
import os

app = Flask(__name__)
mqtt.init_app(app)

@app.route("/")
def index():
    return send_from_directory('../web', 'index.html')

@app.route("/api/start", methods=["POST"])
def start():
    send_command("start")
    return jsonify({"status": "started"})

@app.route("/api/stop", methods=["POST"])
def stop():
    send_command("stop")
    return jsonify({"status": "stopped"})

@app.route("/api/settings", methods=["POST"])
def settings():
    data = request.get_json()
    send_settings(data)
    return jsonify({"status": "settings sent"})

@app.route("/api/status", methods=["GET"])
def status():
    return jsonify(get_status())
