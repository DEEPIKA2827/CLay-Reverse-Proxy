# app.py - Dashboard backend
from flask import Flask, render_template
import os

app = Flask(__name__)
LOG_PATH = r"C:\Users\Deepika\Downloads\CLay-main\CLay-main\logs\attackers.log"  # ✅ correct path

def read_logs():
    data = []
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r") as file:
            for line in file:
                try:
                    parts = line.strip().split("|")
                    timestamp = parts[0].strip()
                    ip_info = parts[1].strip()
                    reputation = parts[2].strip()
                    user_agent = parts[3].strip()

                    ip = ip_info.split("(")[0].replace("IP:", "").strip()
                    location = ip_info.split("(")[1].replace(")", "").strip()

                    data.append({
                        "timestamp": timestamp,
                        "ip": ip,
                        "location": location,
                        "reputation": reputation,
                        "user_agent": user_agent
                    })
                except:
                    continue
    return data

@app.route("/")
def dashboard():
    logs = read_logs()
    return render_template("dashboard.html", logs=logs)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
