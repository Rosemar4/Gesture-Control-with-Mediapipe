# Gesture Control with Mediapipe

This project demonstrates how to use [Mediapipe](https://google.github.io/mediapipe/) and OpenCV for real-time gesture recognition.  
By detecting hand gestures through a webcam, the program can trigger system actions such as **opening file folders** on your PC.  

## ✨ Features
- Real-time hand tracking with Mediapipe
- Gesture recognition mapped to custom actions
- Example: Open folders on your computer using a gesture
- Easily extendable for other controls (e.g., music, browser, apps)

## 🛠️ Technologies
- Python
- Mediapipe
- OpenCV
- OS module

## 📂 Project Structure
gesture-control-mediapipe/
│── main.py # main script
│── gestures/ # (optional) store gesture mapping
│── README.md # project documentation
│── requirements.txt # dependencies

bash
Copy code

## 📦 Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/Gesture-Control-with-Mediapipe.git
   cd Gesture-Control-with-Mediapipe
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the script:

bash
Copy code
python main.py
🚀 Usage
Run the program with your webcam on.

Perform the predefined gestures.

Example: make a ✋ gesture → open a specific folder.

📝 To-Do
Add more gestures

Extend actions beyond opening folders

Optimize gesture recognition
