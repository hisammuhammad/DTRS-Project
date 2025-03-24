# Dynamic Threat Response System (DTRS) - OS Assignment

This is my Operating System assignment project, built for Windows as part of my B.Tech course. The goal was to create a simple system that monitors processes running on the computer, detects potential threats based on high CPU usage, and automatically terminates them to protect the system. It’s a basic example of how an operating system can handle cybersecurity threats autonomously.

## Project Overview
- **Purpose**: To demonstrate OS concepts like process monitoring and management in a practical way.
- **How It Works**: The system checks all running processes every few seconds. If a process uses too much CPU (more than 70%) and isn’t a trusted system process, it’s considered a threat and stopped immediately.
- **Platform**: Designed and tested on Windows.

## Files Included
- **`dtrs.py`**: The main Python script that runs the threat response system. It monitors processes and kills threats.
- **`test_threat.py`** (Optional): A small script I wrote to simulate a threat by using lots of CPU power. You can use it to test `dtrs.py`.
- **`README.md`**: This file! It explains everything about the project.

## How It Works in Detail
1. **Monitoring**: The script uses a library called `psutil` to look at every process running on the computer—like apps, background tasks, or system services.
2. **Threat Detection**: It checks the CPU usage of each process. If any process uses more than 70% CPU and isn’t on a “safe list” (whitelist), it’s flagged as a threat. For example, a virus might use lots of CPU, but normal system processes like `explorer.exe` won’t be flagged.
3. **Response**: Once a threat is found, the script uses the Windows `taskkill` command to stop it forcefully. It’s like telling the OS to shut down the bad process right away.
4. **Looping**: The system keeps running and checking every 2 seconds until you stop it with `Ctrl+C`.

## How to Set Up and Run the Project
Follow these steps to try it on your own Windows computer:

1. **Install Python**:
   - Download Python from [python.org](https://www.python.org/downloads/).
   - Run the installer and make sure to check “Add Python to PATH” (this lets you use Python from Command Prompt).
   - After installing, open Command Prompt and type `python --version` to check it works (e.g., `Python 3.11.5`).

2. **Install the `psutil` Library**:
   - Open Command Prompt (search “cmd” in the Start menu).
   - Type this command and press Enter: