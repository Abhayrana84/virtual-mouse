import cv2
import numpy as np
import pyautogui
from pynput.mouse import Button, Controller
from util import find_distance
import time
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe import Image, ImageFormat

mouse = Controller()
screen_w, screen_h = pyautogui.size()
base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=1)

try:
    landmarker = vision.HandLandmarker.create_from_options(options)
except Exception as e:
    print(f"Hand landmarker not available: {e}")
    print("Attempting to download model...")
    import urllib.request
    import os
    os.makedirs('models', exist_ok=True)
    model_url = 'https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task'
    try:
        urllib.request.urlretrieve(model_url, 'hand_landmarker.task')
        base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
        options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=1)
        landmarker = vision.HandLandmarker.create_from_options(options)
    except:
        print("Failed to download model. Using basic implementation.")
        landmarker = None

cap = cv2.VideoCapture(0)
cooldown = 0

def fingers_up(lm):
    tips = [4,8,12,16,20]
    up = []
    for i in tips:
        up.append(lm[i][1] < lm[i-2][1])
    return up

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture frame")
        break
    
    img = cv2.flip(img, 1)
    h, w, c = img.shape
    
    if landmarker:
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        mp_image = Image(image_format=ImageFormat.SRGB, data=rgb)
        result = landmarker.detect(mp_image)
        
        if result.hand_landmarks:
            for hand_landmarks in result.hand_landmarks:
                lm = []
                for landmark in hand_landmarks:
                    lm.append((int(landmark.x * w), int(landmark.y * h)))
                for idx, point in enumerate(lm):
                    cv2.circle(img, point, 5, (0, 255, 0), -1)
                    if idx in [0, 1, 5, 9, 13, 17]:
                        for next_idx in range(idx + 1, min(idx + 5, 21)):
                            if next_idx < len(lm):
                                cv2.line(img, point, lm[next_idx], (255, 0, 0), 2)
                
                finger_state = fingers_up(lm)
                
                x, y = lm[8]
                mx = np.interp(x, (0, w), (0, screen_w))
                my = np.interp(y, (0, h), (0, screen_h))
                mouse.position = (mx, my)
                if find_distance(lm[8], lm[12]) < 30 and cooldown == 0:
                    mouse.click(Button.left, 1)
                    cooldown = 10
                if finger_state == [False, True, True, True, False] and cooldown == 0:
                    mouse.click(Button.right, 1)
                    cooldown = 10
                if find_distance(lm[4], lm[8]) < 30:
                    pyautogui.scroll(40)
                if finger_state == [False, False, False, False, False] and cooldown == 0:
                    pyautogui.screenshot("screenshot.png")
                    cooldown = 20
    
    cooldown = max(0, cooldown - 1)
    cv2.imshow("AI Virtual Mouse", img)
    
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
