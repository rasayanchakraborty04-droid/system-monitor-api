# 🚀 System Monitor API

A lightweight infrastructure monitoring API built with **Python**, **Flask**, and **Docker**.

This project exposes system-level metrics through REST API endpoints, making it easy to inspect resource usage, environment details, container information, and application health.

Designed as a hands-on project to learn:

* 🐍 Python Backend Development
* 🌐 REST APIs with Flask
* 🐳 Docker & Docker Compose
* 📊 System Monitoring
* ⚙️ DevOps Fundamentals
* 🚀 Containerized Deployments

---

## ✨ Features

### 🩺 Health Monitoring

Check whether the application is running correctly.

```http
GET /health
```

Example Response:

```json
{
  "status": "healthy",
  "service": "system-monitor-api"
}
```

---

### 💻 System Information

Retrieve real-time machine statistics.

```http
GET /system-info
```

Example Response:

```json
{
  "hostname": "rasayan-macbook",
  "cpu_usage": 12.5,
  "memory_usage": 48.2,
  "disk_usage": 67.1
}
```

---

### ⏱️ Uptime Information

View how long the host system has been running.

```http
GET /uptime
```

---

### 🌍 Environment Information

Inspect runtime and platform details.

```http
GET /environment
```

Example Response:

```json
{
  "python_version": "3.13",
  "platform": "Linux",
  "machine": "x86_64",
  "hostname": "container-id"
}
```

---

### 📈 Metrics Dashboard Endpoint

Aggregated monitoring information from a single endpoint.

```http
GET /metrics
```

Example Response:

```json
{
  "system": {
    "hostname": "container-id",
    "platform": "Linux"
  },
  "runtime": {
    "python_version": "3.13"
  },
  "resources": {
    "cpu_percent": 15.4,
    "memory_percent": 52.7,
    "disk_percent": 68.3
  }
}
```

---

## 🏗️ Project Structure

```text
system-monitor-api/
│
├── app.py
├── routes/
│   └── system_routes.py
│
├── services/
│   └── system_service.py
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── README.md
```

---

## 🐳 Running with Docker

### Build the Image

```bash
docker build -t system-monitor-api .
```

### Run the Container

```bash
docker run -p 5000:5000 system-monitor-api
```

Application will be available at:

```text
http://localhost:5000
```

---

## 🐳 Running with Docker Compose

Start the application:

```bash
docker compose up --build
```

Run in detached mode:

```bash
docker compose up -d
```

Stop services:

```bash
docker compose down
```

---

## 🔧 Running Locally

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

---

## 📚 Tech Stack

| Technology     | Purpose                   |
| -------------- | ------------------------- |
| Python         | Core Programming Language |
| Flask          | REST API Framework        |
| psutil         | System Metrics Collection |
| Docker         | Containerization          |
| Docker Compose | Multi-Service Management  |
| GitHub         | Version Control           |

---

## 🎯 Learning Objectives

This project was built to explore:

* Designing REST APIs with Flask
* Collecting system metrics using Python
* Understanding Docker Images & Containers
* Structuring backend applications
* Building DevOps-focused portfolio projects
* Preparing applications for cloud deployment

---

## 🚀 Future Enhancements

* [ ] Network Monitoring Endpoint
* [ ] Container Information Endpoint
* [ ] Process Monitoring
* [ ] Top Memory Consuming Processes
* [ ] Request Logging
* [ ] Swagger/OpenAPI Documentation
* [ ] GitHub Actions CI/CD Pipeline
* [ ] AWS Deployment
* [ ] Prometheus Integration
* [ ] Grafana Dashboard

---

## 👨‍💻 Author

Built by **Rasayan Chakraborty** as part of a hands-on journey into Backend Engineering, Cloud Infrastructure, Docker, and DevOps.

⭐ If you found this project useful, consider giving it a star.
