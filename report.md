# Project Report: Secure Web Application with Intrusion Detection and Log Monitoring

## 1. Introduction
The goal of this project was to create a **secure web application** that integrates **intrusion detection** and **log monitoring** capabilities. The application demonstrates best practices in cybersecurity, including secure authentication, log analysis, and real-time monitoring using open-source tools. The project was designed to showcase skills in **software development**, **system administration**, and **cybersecurity**, making it a strong portfolio piece for a cybersecurity co-op or job application.

---

## 2. Objectives
The project aimed to achieve the following:
1. **Develop a Secure Web Application:**
   - Build a Flask-based web application with secure authentication (password hashing).
   - Implement HTTPS for secure communication.

2. **Set Up Intrusion Detection:**
   - Use **Suricata** (an open-source IDS) to monitor network traffic for suspicious activity.

3. **Implement Log Monitoring:**
   - Use the **ELK Stack** (Elasticsearch, Logstash, Kibana) to collect, process, and visualize logs.

4. **Deploy the Application:**
   - Deploy the application on an **AWS EC2 instance**.
   - Set up a **CI/CD pipeline** using GitHub Actions for automated deployment.

5. **Document the Process:**
   - Provide step-by-step instructions for setting up and running the project.
   - Explain the purpose and outcomes of each component.

---

## 3. Technologies Used
- **Web Application Framework:** Flask (Python)
- **Authentication:** Bcrypt (password hashing)
- **Intrusion Detection System (IDS):** Suricata
- **Log Monitoring:** ELK Stack (Elasticsearch, Logstash, Kibana)
- **Deployment:** AWS EC2, Docker, Docker Compose
- **Version Control:** Git, GitHub
- **CI/CD:** GitHub Actions

---

## 4. Implementation

### 4.1 Secure Web Application
- **Flask Web App:**
  - A simple web application was built using Flask.
  - Features include a login page with secure authentication using **bcrypt** for password hashing.
  - HTTPS was enabled for secure communication.


