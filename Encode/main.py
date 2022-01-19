import mediapipe as mp
import cv2
import time
import numpy as np
import os
import matplotlib.pyplot as plt
import winsound

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

cap = cv2.VideoCapture(0)

mp_draw = mp.solutions.drawing_utils

path_model = "E:\Project\depthmap\model-f6b98070.onnx"

model = cv2.dnn.readNet(path_model)

def hand_detection(image):
    with mp_holistic.Holistic(min_tracking_confidence=0.6, min_detection_confidence=0.6) as holistic:

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        result = holistic.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        mp_drawing.draw_landmarks(image, result.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                                  landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255, 255, 0), thickness=2,
                                                                               circle_radius=3),
                                  connection_drawing_spec=mp_drawing.DrawingSpec(color=(150, 150, 0), thickness=2,
                                                                                 circle_radius=2))

        mp_drawing.draw_landmarks(image, result.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                                  landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255, 255, 0), thickness=2,
                                                                               circle_radius=3),
                                  connection_drawing_spec=mp_drawing.DrawingSpec(color=(150, 150, 0), thickness=2,
                                                                                 circle_radius=2))

        lh = result.left_hand_landmarks
        rh = result.right_hand_landmarks

        cv2.imshow('hand_detection', image)

        if(lh!=None or rh!=None):
            return True

        return False


def line_detection(image_final, main):

    c2 = np.histogram(image_final.ravel(), 256, [0, 256])

    c1 = np.histogram(main.ravel(), 256, [0, 256])

    diff = c1[0] - c2[0]
    diff = np.delete(diff, 0)
    diff = np.sum(diff)

    if diff > 600:
        time.sleep(0.5)
        return True
    else:
        return False

def Depth_map(image):
    Height, Width, channels = image.shape

    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    blob = cv2.dnn.blobFromImage(img, 1 / 255., (384, 384), (123.675, 116.28, 103.53), True, False)

    model.setInput(blob)

    depth_map = model.forward()

    depth_map = depth_map[0, :, :]
    depth_map = cv2.resize(depth_map, (Width, Height))

    depth_map = cv2.normalize(depth_map, None, 0, 1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    return depth_map


if __name__ == '__main__':
    counter = 0
    main =0
    x=0
    while cap.isOpened():
        counter+=1
        ret, image = cap.read()
        R_hand_detection = hand_detection(image)

        c = 0
        image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(image_hsv,
                           np.array([100, 100, 50]),
                           np.array([120, 255, 255]))
        image_final = cv2.bitwise_and(image, image, mask=mask)

        if counter < 5:
            main = image_final

        R_line_detection = line_detection(image_final, main)

        R_Depth_map = Depth_map(image)

        cv2.imshow('original image', image)
        cv2.imshow('line detection', image_final)
        cv2.imshow('Depth map', R_Depth_map)

        if R_line_detection==True and R_hand_detection==True:
            x+=1
            print("window down " + str(x) +" !!!!!!!!!!!")
            winsound.Beep(440, 600)


        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()













