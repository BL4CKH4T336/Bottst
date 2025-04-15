# app.py
from flask import Flask
import threading
import watchdog

app = Flask(__name__)

@app.route("/")
def home():
    return "Telegram bot watchdog is running."

def start_watchdog():
    watchdog.monitor_bot()

if __name__ == "__main__":
    thread = threading.Thread(target=start_watchdog, daemon=True)
    thread.start()
    app.run(host="0.0.0.0", port=5000)
