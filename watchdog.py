# watchdog.py
import subprocess
import time

def run_bot():
    return subprocess.Popen(["python", "bot.py"])

def monitor_bot():
    process = run_bot()
    while True:
        time.sleep(600)  # 10 minutes
        if process.poll() is not None:
            print("Bot stopped. Restarting...")
            process = run_bot()

if __name__ == "__main__":
    monitor_bot()
