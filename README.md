Multi-Node Puppet Deployment Simulator

Student Name: Himani Choudhary
Reg. No.: 23FE10CSE00827
Course: CSE DevOps
Semester: VI
Project Type: DevOps Simulation Project


Project Overview

The Multi-Node Puppet Deployment Simulator is a DevOps-based project that simulates configuration management and deployment across multiple nodes using a Puppet-like approach.

Instead of using real infrastructure, this project uses a lightweight simulation to demonstrate how deployments occur across multiple systems in a distributed environment.


 Problem Statement

Managing deployments across multiple servers is complex and error-prone. This project demonstrates how automation tools like Puppet can help manage and monitor deployments efficiently.

Objectives
	•	Simulate deployment across multiple nodes
	•	Visualize node status using a dashboard
	•	Implement REST API for deployment trigger
	•	Demonstrate DevOps practices (CI/CD, Docker, testing)

Key Features
	•	 Dashboard for node status visualization
	•	 Randomized deployment simulation
	•	 REST API (/api/deploy)
	•	 Docker support
	•	 CI/CD pipeline using GitHub Actions
	•	 Unit testing with pytest


Technology Stack

Core Technologies
	•	Programming Language: Python
	•	Framework: Flask
	•	Frontend: HTML, CSS
	•	Database: None (Simulation-based)

DevOps Tools
	•	Version Control: Git & GitHub
	•	CI/CD: GitHub Actions
	•	Containerization: Docker
	•	Orchestration: Kubernetes (basic config)
	•	Configuration Management: Puppet (simulated)
	•	Monitoring: Nagios (config files)


Access the Application
	•	Dashboard: http://127.0.0.1:8080
	•	API: http://127.0.0.1:8080/api/deploy

Testing
  Tests include:
	•	API response validation
	•	Node data verification

CI/CD Pipeline

The project uses GitHub Actions for CI/CD.

Pipeline Stages:
	1.	Code Checkout
	2.	Setup Python
	3.	Install Dependencies
	4.	Run Tests
	5.	Build Docker Image

Pipeline runs automatically on every push.

Security
	•	Input validation (basic)
	•	Environment-based config (placeholder)
	•	Dependency management

Challenges
	1.	Setting up project structure
	2.	Integrating CI/CD pipeline
	3.	Debugging Flask API

Learnings
	•	DevOps lifecycle understanding
	•	CI/CD pipeline creation
	•	Docker basics
	•	API development using Flask

Demo
	•	Run the project
	•	Click Run Deployment
	•	Observe node status changes

Acknowledgments
	•	Course Instructor
	•	Open-source tools
	•	Online tutorials
