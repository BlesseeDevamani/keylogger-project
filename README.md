# Python Keylogger
## Overview
This project is a basic Python-based keylogger developed for educational and cybersecurity research purposes. It captures all keystrokes made by the user and logs them into timestamped files.
> *Note:* This software is intended *only for ethical use* in penetration testing or cybersecurity labs. Do not deploy without user consent.
---
## Features
- Records all keyboard input
- Logs are timestamped and saved to disk
- Uses the pynput library for keyboard listening
- Automatically stops when ESC key is pressed
- Logs stored in a dedicated logs/ directory
---
## Installation
### Prerequisites
- Python 3.x
- pip (Python package manager)

### Install Dependencies

```bash
pip install pynput


---

Usage

Run the Keylogger

python keylogger.py

Press ESC to stop the keylogger.

Logs are saved to logs/keystrokes_<timestamp>.txt.



---

File Structure

keylogger-project/
│
├── keylogger.py          # Main keylogger logic
├── logs/                 # Directory containing keystroke logs
├── .gitignore            # Files and folders to ignore in git
└── README.md             # Project documentation


---

Logging Format

Each keypress is logged with a timestamp:

2025-05-21 12:00:45,303: Key pressed: a
2025-05-21 12:00:45,404: Key pressed: b
2025-05-21 12:00:45,506: Special key pressed: Key.space


---

Git Commands

git init
git add .
git commit -m "Initial commit: Python keylogger"
git branch -M main
git remote add origin https://github.com/your-username/keylogger-project.git
git push -u origin main

