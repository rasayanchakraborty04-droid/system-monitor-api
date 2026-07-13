from flask import Flask
import socket
import psutil

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "System monitoring API"
    }

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "service": "system-monitor-api"
    }

@app.route("/system-info")
def system_info():
    hostname = socket.gethostname()
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')

    return {
        "hostname": hostname,
        "cpu_usage": cpu_usage,
        "memory": {
            "total": memory_info.total,
            "available": memory_info.available,
            "used": memory_info.used,
            "percent": memory_info.percent
        },
        "disk": {
            "total": disk_info.total,
            "used": disk_info.used,
            "free": disk_info.free,
            "percent": disk_info.percent
        }
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)