# 🤖 Gesture-Based Math Solver 

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


1. Clone the repository:
bash
Copy
Edit
git clone https://github.com/RamakrishnaTanam/Gesture-Based-Math-Solver.git
cd Gesture-Based-Math-Solver
2. Create and activate a virtual environment:
For Windows:

bash
Copy
Edit
python -m venv venv
.\venv\Scripts\activate
For macOS/Linux:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
3. Install dependencies:
bash
Copy
Edit
pip install -r requirements.txt
4. Run the Streamlit app:
bash
Copy
Edit
streamlit run app.py
