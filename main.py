import Gesture_recognition
import cv2

if __name__ == '__main__':
    #Gesture_recognition.detect()
    cap = cv2.VideoCapture(0)
    print(1)
    while True:
        ret,frame = cap.read()   #返回ret是bool值代表是否截取到，frame是截取的这一帧
        gesture = Gesture_recognition.detect_hand(frame)
        print(gesture)
