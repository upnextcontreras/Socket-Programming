# CPSC 471 - Socket Programming and Multithreading Assignments

## Overview
This repository contains solutions for two assignments from the CPSC 471 course (Computer Networks) at California State University, Fullerton, focusing on socket programming, HTTP communication, and multithreading concepts.

### Assignments Included:
- **Homework 2:** Introduction to Socket Programming and HTTP
- **Homework 3:** Multithreaded Socket Programming and HTTP

---

## Homework 2: Socket Programming Web Server

### Objective
Create a basic web server using TCP sockets to handle HTTP requests and responses.

### Key Requirements
- Server must display verbose debugging information:
  - IP address and port on startup.
  - Notification of client connections with client IP address and HTTP request.
  - File contents are displayed if the file is found.
  - Clear error message and HTTP "404 Not Found" response if the file is not found.
- Option to keep the server running continuously or terminate after handling a request.

### Implementation Details
- **Language used:** Python
- **Test environment:** Small HTML/text files tested using a web browser.

### How to Run
1. Clone the repository:
   ```bash
   git clone [repo-url]
   
2. Run the server:
   ```bash
   python webserver.py
   
### Submission Components

- Source code (webserver.py)
- Screenshots demonstrating successful and unsuccessful HTTP requests.
- Explanation and validation of server functionality.

<img width="638" alt="HelloWord" src="https://github.com/user-attachments/assets/1f2a8f55-2d88-483e-b6b6-bf5edb4078d8" />
<img width="290" alt="HelloWord(1)" src="https://github.com/user-attachments/assets/bd29f136-620f-4a65-b841-b9c2025d625c" />
<img width="448" alt="HellowWord(2)" src="https://github.com/user-attachments/assets/c5a1a504-f0ed-4b45-9f2f-b91ea180a782" />

<img width="645" alt="404notfound" src="https://github.com/user-attachments/assets/e0801c13-90db-4025-8c57-63a797570f2e" />
<img width="290" alt="404notfound(1)" src="https://github.com/user-attachments/assets/b8f85a35-5186-4146-9554-60ed72e215b9" />



## Homework 3: Multithreaded Web Server

### Objective
Extend Homework 2 to create a multithreaded web server, capable of handling multiple HTTP requests concurrently.

### Key Requirements
- Multithreaded server design:
  - The server continuously listens for client connections.
  - Creates a new thread for each client connection.
  - Verbose debugging includes thread creation, thread termination, client IP, HTTP requests, and file handling outcomes.

### Implementation Details
- **Language used:** Python
- **Threading approach:** Each incoming connection is managed by an independent thread to prevent new requests from being blocked.

### How to Run
1. Clone the repository:
   ```bash
   git clone [repo-url]
   
2. Run the server:
   ```bash
   python webserver.py
   
### Submission Components

- Source code (threaded_webserver.py)
- Screenshots demonstrating concurrent handling of HTTP requests, both successful and 404 errors.
- Detailed explanation validating correct multithreaded behavior.
- Explanation of the threading model and communication between threads and clients.

## Academic Integrity and Purpose

This repository contains assignment solutions completed as part of coursework for the CPSC 471 class at California State University, Fullerton. The code provided here is intended solely for educational purposes, demonstrating my understanding of socket programming, HTTP protocol handling, and multithreading concepts.  
These projects are displayed publicly to illustrate my comprehension of key networking and software engineering principles as taught in the course. Any reuse of this code must comply with academic integrity guidelines and proper citation practices.
