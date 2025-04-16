# CPSC 471 - Socket Programming and Multithreading Assignments

## Overview
This repository contains solutions for two assignments from the CPSC 471 course (Computer Networks) at California State University, Fullerton, focusing on socket programming, HTTP communication, and multithreading concepts.

### Assignments Included:
- **Homework 2:** Introduction to Socket Programming and HTTP
- **Homework 3:** Multithreaded Socket Programming and HTTP

---

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
