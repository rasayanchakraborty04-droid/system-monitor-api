from datetime import datetime
from flask import Flask
import socket
import psutil
import platform
import sys

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "System monitoring API",
        "available_endpoints": [
            "/health",
            "/system-info",
            "/uptime"
            "/environment"
        ]
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
    boot_time = psutil.boot_time()

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
        },
        "boot_time": datetime.fromtimestamp(boot_time).strftime("%Y-%m-%d %H:%M:%S")
    }

@app.route("/uptime")
def uptime():
    boot_time = psutil.boot_time()
    uptime_seconds = (datetime.now() - datetime.fromtimestamp(boot_time)).total_seconds()
    uptime_string = str(datetime.now() - datetime.fromtimestamp(boot_time)).split('.')[0]

    return {
        "uptime_seconds": uptime_seconds,
        "uptime_string": uptime_string
    }

@app.route("/environment")
def environment():
    return {
        "python_version": sys.version,
        "platform": platform.system(),
        "platform_release": platform.release(),
        "platform_version": platform.version(),
        "architecture": platform.architecture(),
        "processor": platform.processor()
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)