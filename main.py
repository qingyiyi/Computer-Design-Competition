import Gesture_recognition
import cv2
import describe_vision
import pyautogui
import chatsystem
import threading
import time
import queue

def module_Gesture_recognition():
    cap = cv2.VideoCapture(0)
    print(1)
    while True:
        ret,frame = cap.read()   #返回ret是bool值代表是否截取到，frame是截取的这一帧
        gesture = Gesture_recognition.detect()

def module_Describe_vision():
    im = pyautogui.screenshot()
    im.save("test.jpg")
    status = describe_vision.describe_photo('test.jpg')
    q.put(status['name'])
    return status['name']

def module_Chat_system(text):
    reply = chatsystem.chat(text)
    q.put(reply)
    return reply

if __name__ == '__main__':
        global q 
        q= queue.Queue()
    #while(True):
        print('开始录音')
        detect = chatsystem.Monitor_MIC(250,'audio')
        if(detect != 1):
            print('你说话啊！')
            time.sleep(5)
        else:
            Thread_list = []
            text = chatsystem.convert('audio.wav','base')
            text='描述'
            print(text)
            if ('鼠标' in text or '控制' in text):
                p1 = threading.Thread(name = 'p1', target=module_Gesture_recognition, args=())
                Thread_list.append(p1)
            elif '描述' in text:
                p2 = threading.Thread(name = 'p2', target=module_Describe_vision, args=())
                Thread_list.append(p2)
            else:
                p3 = threading.Thread(name = 'p3', target=module_Chat_system, args=(text))
                Thread_list.append(p3)
            for thread in Thread_list:
                thread.start()
            for thread in Thread_list:
                thread.join()
            result = q.get()
            print(result)
            time.sleep(5)