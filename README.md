#  Gesture-Based Math Solver 

A real-time math-solving app using hand gestures powered by **OpenCV**, **MediaPipe**, and **Google Gemini AI**.

## Features
- Draw math problems in the air using your hand
- Recognizes equations via webcam with `cvzone` + `mediapipe`
- Solves them using Google's **Gemini Generative AI**
- Built with Streamlit for a responsive web UI



##  Technologies Used
- `Python 3.10`
- `Streamlit`
- `OpenCV`
- `cvzone` (for hand tracking)
- `MediaPipe`
- `Google Generative AI API` (Gemini)

##  Running the App Locally


To use this project, follow these steps:

Clone the repository: git clone   (https://github.com/RamakrishnaTanam/Gesture-Based-Math-Solver.git)

Install the required packages: pip install -r requirements.txt

Add your Google API key to the .env file.

Run the Streamlit app: streamlit run app.py

Access the app in your browser at http://localhost:8501
