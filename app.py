import cvzone
import numpy as np
import cv2
import google.generativeai as genai
from cvzone.HandTrackingModule import HandDetector
from api import api_no
from PIL import Image
import streamlit as st

st.set_page_config(layout="wide")
st.image('background.jpg')

col1, col2 = st.columns([3,2])

with col1:
    run = st.checkbox('Run', value=True)
    FRAME_WINDOW = st.image([])

with col2:
    output_text_area = st.title("Answer")
    output_text_area = st.subheader("")



genai.configure(api_key ="AIzaSyDQhv9zh43zE1f_n8cJ8z0to6f_hkTF1CE" )  #change this to your api_key
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize the webcam to capture video
# The '2' indicates the third camera connected to your computer; '0' would usually refer to the built-in camera
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)

def getHandInfo(img):
    # Find hands in the current frame
    hands, img = detector.findHands(img, draw=False, flipType=True)

    # Check if any hands are detected
    if hands:
        # Information for the first hand detected
        hand1 = hands[0]  # Get the first hand detected
        lmList = hand1["lmList"]  # List of 21 landmarks for the first hand

        # Count the number of fingers up for the first hand
        fingers = detector.fingersUp(hand1)
        print(fingers)
        return fingers, lmList
    else:
        return None

def draw(info, prev_pos, canvas):
    fingers, lmList = info
    current_pos = None # to reset the finger if it go down and go up again
    if fingers == [0, 1, 0, 0, 0]:

        current_pos = lmList[8][0:2]
        if prev_pos is None: prev_pos = current_pos
        cv2.line(canvas, current_pos, prev_pos, color=(255,0,255), thickness=6)
    elif fingers == [1, 0, 0, 0, 1]:
        canvas = np.zeros_like(img)

    return current_pos, canvas

def sendToAI(model, canvas, fingers):
    if fingers == [1, 1, 1, 1, 0]:
        PIL_image = Image.fromarray(canvas)
        response = model.generate_content(["Solve this math problem", PIL_image])
        return response.text

prev_pos = None
canvas = None
image_combined = None
output_text = ""

# Continuously get frames from the webcam
while True:
    # Capture each frame from the webcam
    # 'success' will be True if the frame is successfully captured, 'img' will contain the frame
    success, img = cap.read()
    img = cv2.flip(img, 1)

    if canvas is None: 
        canvas = np.zeros_like(img)


    info = getHandInfo(img)
    if info:
        fingers, lmList = info
        prev_pos, canvas = draw(info, prev_pos, canvas)
        output_text = sendToAI(model, canvas, fingers)

    image_combined = cv2.addWeighted(img, 0.7, canvas, 0.3, 0)
    FRAME_WINDOW.image(image_combined, channels="BGR")

    if output_text:
        output_text_area.text(output_text)

    # Keep the window open and update it for each frame; wait for 1 millisecond between frames
    cv2.waitKey(1)