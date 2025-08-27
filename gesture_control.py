r"""
    Date: 14th July 2025
    AUthor: Rosey

    Aim: To use my gestures to open an application on my pc.

    Technicalities: - use pretrained model, media pipe
        -- access webcam with openCV
        -- open file folder/ an app from my PC

    Job Status: FINISHED
    Shege's: 
        -- cannot install mediapipe on python 3.13
            ## to check version
                py --version 
        -- had to use a virtual environment
            ##create a venv
                py -3.10 -m venv gesture-env
            ## activate it
                .\gesture-env\Scripts\activate
            ## get mediapipe
                pip install mediapipe opencv-python
                (gesture-env) PS C:\Users\user\Documents\Computer Vision,Python projects\Gesture control with fingers> 
            ## run final script
                python gesture_unlock.py
"""

#import libraries
import cv2
import mediapipe as mp
import os

# Initialize Mediapipe hand detection
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Start webcam
cap = cv2.VideoCapture(0)

unlocked = False   

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)   
    #converts color to gray scale
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_img)   

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                lm_list.append((int(lm.x * w), int(lm.y * h)))

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            if lm_list:
                fingers = []

                # Thumb: compare x-coordinate
                fingers.append(lm_list[4][0] > lm_list[3][0])
                # Other fingers: compare y-coordinate (tip above pip joint)
                fingers.append(lm_list[8][1] < lm_list[6][1])   # Index
                fingers.append(lm_list[12][1] < lm_list[10][1]) # Middle
                fingers.append(lm_list[16][1] < lm_list[14][1]) # Ring
                fingers.append(lm_list[20][1] < lm_list[18][1]) # Pinky

                # If all 5 fingers are up and it hasn't been unlocked yet
                if all(fingers) and not unlocked:
                    cv2.putText(img, "Access Granted", (50, 100),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
                    print("Access Granted!")
                    os.system("start explorer")  # Open File Explorer
                    unlocked = True  # Lock this so it doesn't keep triggering

    else:
        unlocked = False  # No hand detected — reset unlock

    cv2.imshow("Gesture Unlock", img)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
