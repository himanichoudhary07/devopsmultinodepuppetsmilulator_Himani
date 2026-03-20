# 🚀 Multi-Node Puppet Deployment Simulator

![CI/CD](https://img.shields.io/badge/CI-CD-Pipeline-success-brightgreen)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)

---

## 👩‍💻 Student Details

**Student Name:** Himani Choudhary  
**Registration No.:** 23FE10CSE00827  
**Course:** CSE DevOps  
**Semester:** VI  
**Project Type:** DevOps Simulation Project  

---

## 📌 Project Overview

The **Multi-Node Puppet Deployment Simulator** is a DevOps-based project that simulates configuration management and deployment across multiple nodes using a Puppet-like approach.

Instead of using real infrastructure, this project provides a lightweight simulation to demonstrate how deployments occur across distributed systems in an automated environment.

---

## ❗ Problem Statement

Managing deployments across multiple servers is complex and error-prone.  
This project demonstrates how automation tools like Puppet can streamline deployment, improve consistency, and reduce manual intervention.

---

## 🎯 Objectives

- Simulate deployment across multiple nodes  
- Visualize node status using a dashboard  
- Implement REST API for deployment trigger  
- Demonstrate DevOps practices (CI/CD, Docker, testing)  

---

## ✨ Key Features

- 📊 Interactive dashboard for node status visualization  
- 🔄 Randomized deployment simulation  
- 🌐 REST API endpoint (`/api/deploy`)  
- 🐳 Docker-based containerization  
- ⚙️ CI/CD pipeline using GitHub Actions  
- 🧪 Unit testing using pytest  

---

## 🛠️ Technology Stack

### 🔹 Core Technologies
- **Programming Language:** Python  
- **Framework:** Flask  
- **Frontend:** HTML, CSS  
- **Database:** None (Simulation-based)  

### 🔹 DevOps Tools
- **Version Control:** Git & GitHub  
- **CI/CD:** GitHub Actions  
- **Containerization:** Docker  
- **Orchestration:** Kubernetes (basic configuration)  
- **Configuration Management:** Puppet (simulated)  
- **Monitoring:** Nagios (configuration files)  

---

## 🚀 Access the Application

- **Dashboard:** http://127.0.0.1:8080  
- **API:** http://127.0.0.1:8080/api/deploy  

---

## 🧪 Testing

Test cases include:

- API response validation  
- Node deployment status verification  

Run tests using:

```bash
pytest tests/