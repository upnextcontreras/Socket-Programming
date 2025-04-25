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
