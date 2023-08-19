import cv2
import mediapipe as mp
import time
import math
from pyfirmata import Arduino, util,OUTPUT
import test3 as t

def map_value(value, in_min, in_max, out_min, out_max):
    # Map the value from the input range to the output range
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min



board = Arduino("COM11")
#analog_pin=2
#board.analog[analog_pin].mode = OUTPUT
analog_output_pin = board.get_pin('d:6:o')
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
detector = t.handDetector()

while True:
    ret, frame = cap.read()
    frame= cv2.flip(frame,1)
    frame=detector.findHands(frame)
    lmList, bbox = detector.findPosition(frame)
    cv2.imshow('camera', frame)
    
    if len(lmList)!=0:
        length,frame,lineInfo =detector.findDistance(4, 8, frame)
        if length>132 :
            length = 132
        elif length<8:
            length = 8
        mp=map_value(length, 8, 132, 0, 255)
        mp=int(mp)
        analog_output_pin.write(mp)
        #time.sleep(0.5)
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

 
cap.release()
cv2.destroyAllWindows() 