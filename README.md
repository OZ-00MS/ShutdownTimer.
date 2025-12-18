# 🕒 Shutdown Timer (Python)

A simple **PC Shutdown Timer** built with **Python** using **Tkinter**.  
Users can schedule or cancel a shutdown directly from a friendly GUI.  
This project can also be converted into a standalone **Windows EXE** using **PyInstaller** — no Python installation required for users.

---
### 📸 Preview
<img width="404" height="481" alt="Screenshot 2025-12-18 195944" src="https://github.com/user-attachments/assets/9f3b2b6f-40c6-464f-8a63-3b73a689a619" />


```md
![Shutdown Timer Preview](./images/preview.png)
You can name the image preview.png

Place the image in the images/ folder inside your project

Open main.py (or run the EXE) to see:

Schedule shutdown buttons (5, 10, 15, 20, 30, 40 min)

Cancel shutdown button

Simple footer: “with OZ ❤️ in Python”

🧰 Technologies Used
Python 3.10–3.14

Tkinter for GUI

PyInstaller (optional, for EXE packaging)

❌ No external frameworks required
❌ Optional EXE build for users without Python

📁 Project Structure
bash
Copier le code
/ShutdownTimer
│
├── main.py         # Main Python script
├── images/         # Screenshots or icons
├── music/          # Optional background music
├── README.md       # Project documentation
└── .gitignore      # Ignore dist/build files
▶️ How to Run
Option 1: Run with Python
Make sure Python 3.10–3.14 is installed

Clone or download the project

Run the app:

bash
Copier le code
python main.py
Option 2: Run as Standalone EXE (Windows)
Install PyInstaller:

bash
Copier le code
pip install pyinstaller
From the project folder, run:

bash
Copier le code
python -m PyInstaller --onefile --add-data "images;images" main.py
After it finishes, find the EXE in the dist/ folder

Users can run the EXE without installing Python

To include music folder:

bash
Copier le code
python -m PyInstaller --onefile --add-data "images;images" --add-data "music;music" main.py
🖱 Controls / Usage
Click a button → Schedule shutdown for that time

Click Cancel Shutdown → Abort timer

Footer shows: “with OZ ❤️ in Python”

🧪 Features
Easy schedule buttons (5–40 min)

Cancel shutdown anytime

Clean, beginner-friendly GUI

Optional background music (can be disabled)

Can create standalone Windows EXE

🛠 Possible Improvements
Add custom timer input

Add notification popup before shutdown

Add sound alert before shutdown

Dark/light theme toggle

👤 Author
Oz
Web Developer & Mobile App Student

📜 License
This project is open-source and free to use for learning purposes.

⭐ If you like this project, give it a star on GitHub!

yaml
Copier le code

---

If you want, I can **also create a ready GitHub folder structure** with this README, placeholder `images/` folder, `main.py`, and `.gitignore` so you can push everything at once.  

Do you want me to do that?
