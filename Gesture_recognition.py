import cv2
import mediapipe as mp
import math
import pyautogui
import pyperclip
pyautogui.FAILSAFE=False

import threading 

def vector_3d_angle(angle_list,v1,v2):
    pthread = threading.current_thread()
    v1_x=v1[0]
    v1_y=v1[1]
    v1_z=v1[2]
    v2_x=v2[0]
    v2_y=v2[1]
    v2_z=v2[2]
    try:
        angle_= math.degrees(math.acos((v1_x*v2_x+v1_y*v2_y+v1_z*v2_z)/(((v1_x**2+v1_y**2+v1_z**2)**0.5)*((v2_x**2+v2_y**2+v2_z**2)**0.5))))
    except:
        angle_ =65535.
    if angle_ > 180.:
        angle_ = 65535.
    # return angle_
    if(pthread.name == 'p1'):
        angle_list[0] = angle_
    elif(pthread.name == 'p2'):
        angle_list[1] = angle_
    elif(pthread.name == 'p3'):
        angle_list[2] = angle_
    elif(pthread.name == 'p4'):
        angle_list[3] = angle_
    elif(pthread.name == 'p5'):
        angle_list[4] = angle_

def hand_angle(hand_):
    '''
        获取对应手相关向量的二维角度,根据角度确定手势
    '''
    angle_list = [0] * 5
    Thread_list = []
    #---------------------------- thumb 大拇指角度
    p1 = threading.Thread(name = 'p1', target=vector_3d_angle, args=(
        angle_list,
         ((int(hand_[0][0])- int(hand_[2][0])), (int(hand_[0][1])- int(hand_[2][1])), (int(hand_[0][2])- int(hand_[2][2]))),
         ((int(hand_[3][0])- int(hand_[4][0])), (int(hand_[3][1])- int(hand_[4][1])), (int(hand_[3][2])- int(hand_[4][2])))
         ))
    Thread_list.append(p1)

    #---------------------------- index 食指角度
    p2 = threading.Thread(name = 'p2', target=vector_3d_angle, args=(
        angle_list,
        ((int(hand_[0][0])- int(hand_[5][0])), (int(hand_[0][1])- int(hand_[5][1])), (int(hand_[0][2])- int(hand_[5][2]))),
        ((int(hand_[7][0])- int(hand_[8][0])), (int(hand_[7][1])- int(hand_[8][1])), (int(hand_[7][2])- int(hand_[8][2])))
        ))
    Thread_list.append(p2)

    #---------------------------- middle 中指角度
    p3 = threading.Thread(name = 'p3', target=vector_3d_angle, args=(
        angle_list,
        ((int(hand_[0][0])- int(hand_[9][0])), (int(hand_[0][1])- int(hand_[9][1])), (int(hand_[0][2])- int(hand_[9][2]))),
        ((int(hand_[11][0])- int(hand_[12][0])), (int(hand_[11][1])- int(hand_[12][1])), (int(hand_[11][2])- int(hand_[12][2])))
        ))
    Thread_list.append(p3)

    #---------------------------- ring 无名指角度
    p4 = threading.Thread(name = 'p4', target=vector_3d_angle, args=(
        angle_list,
         ((int(hand_[0][0])- int(hand_[13][0])), (int(hand_[0][1])- int(hand_[13][1])), (int(hand_[0][2])- int(hand_[13][2]))),
        ((int(hand_[13][0])- int(hand_[16][0])),(int(hand_[13][1])- int(hand_[16][1])), (int(hand_[13][2])- int(hand_[16][2])))
        ))
    Thread_list.append(p4)

    #---------------------------- pink 小拇指角度
    p5 = threading.Thread(name = 'p5', target=vector_3d_angle, args=(
        angle_list,
         ((int(hand_[0][0])- int(hand_[17][0])),(int(hand_[0][1])- int(hand_[17][1])), (int(hand_[0][2])- int(hand_[17][2]))),
        ((int(hand_[17][0])- int(hand_[20][0])),(int(hand_[17][1])- int(hand_[20][1])), (int(hand_[17][2])- int(hand_[20][2])))
        ))
    Thread_list.append(p5)
    for thread in Thread_list:
        thread.start()
    for thread in Thread_list:
        thread.join()
    return angle_list

def h_gesture(angle_list):
    '''
        # 二维约束的方法定义手势
        # fist five gun love one six three thumbup yeah
    '''
    thr_angle = 25.
    thr_angle_thumb = 45.
    thr_angle_s = 30.
    gesture_str = None
    if 65535. not in angle_list:
        if (angle_list[0]<thr_angle_s) and (angle_list[1]<thr_angle_s) and (angle_list[2]<thr_angle_s) and (angle_list[3]<thr_angle_s) and (angle_list[4]<thr_angle_s):
            gesture_str = "roll up/down"
        elif (angle_list[0]>thr_angle_thumb) and (angle_list[1]>thr_angle) and (angle_list[2]>thr_angle) and (angle_list[3]>thr_angle) and (angle_list[4]>thr_angle):
            gesture_str = "move mouse"
        elif (angle_list[0]<thr_angle_s)  and (angle_list[1]>thr_angle) and (angle_list[2]>thr_angle) and (angle_list[3]>thr_angle) and (angle_list[4]>thr_angle):
            gesture_str = "left click"
        elif (angle_list[0]>thr_angle_thumb)  and (angle_list[1]<thr_angle_s) and (angle_list[2]>thr_angle) and (angle_list[3]>thr_angle) and (angle_list[4]>thr_angle):
            gesture_str = "right click"
    return gesture_str

def hand_coordinate(hand_local, hand_landmarks, frame):
    tthread = threading.current_thread()
    step = 3
    if(tthread.name == 't1'):
        start = 0
    elif(tthread.name == 't2'):
        start = 1
    elif(tthread.name == 't3'):
        start = 2
    for i in range(7):
        x = hand_landmarks.landmark[start+i*step].x*frame.shape[1]
        y = hand_landmarks.landmark[start+i*step].y*frame.shape[0]
        z = hand_landmarks.landmark[start+i*step].z
        hand_local[start+i*step] = (x,y,z)

def mouse_control(gesture_str, hand_local):
    left, right, up, down = 0.4, 0.7, 0.4, 0.8
    width,height = pyautogui.size()
    
    if(hand_local[0]<left): x = 0
    elif(hand_local[0]>right): x = 1
    else: x = (hand_local[0] - left)/(right - left)

    if(hand_local[1]<up): y = 0
    elif(hand_local[1]>down): y = 1
    else: y = (hand_local[1] - up)/(down - up)

    x = math.ceil(x * width) 
    y = math.ceil(y * height)
    #分指令控制
    if(gesture_str == "roll up/down"):
        if(hand_local[1]<0.5): 
            pyautogui.scroll(100)
        else:
            pyautogui.scroll(-100)
    elif(gesture_str == "move mouse"):    
        pyautogui.moveTo(x,y,duration=0.001)
    elif(gesture_str == "left click"):
        pyautogui.click(x,y,button='left') ##点击具体坐标的鼠标左键
    elif(gesture_str == "right click"):
        pyautogui.click(x,y,button='right') ##点击具体坐标的鼠标右键    

def detect():
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5)
    cap = cv2.VideoCapture(0)
    while True:
        ret,frame = cap.read()   #返回ret是bool值代表是否截取到，frame是截取的这一帧
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)   #改变颜色空间
        frame= cv2.flip(frame,1)              #图片水平镜像翻转
        results = hands.process(frame)        #检测手
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)   #转换回去

        if results.multi_hand_landmarks:    #检测到手
            for hand_landmarks in results.multi_hand_landmarks:      
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)   #绘制图像
                hand_local = [0] * 22      
                tthread_list = []
                # for i in range(21):
                #     x = hand_landmarks.landmark[i].x*frame.shape[1]
                #     y = hand_landmarks.landmark[i].y*frame.shape[0]
                #     z = hand_landmarks.landmark[i].z
                #     hand_local[i] = (x,y,z)
                t1 = threading.Thread(name = 't1', target = hand_coordinate, args=(hand_local, hand_landmarks, frame))
                tthread_list.append(t1)
                t2 = threading.Thread(name = 't2', target = hand_coordinate, args=(hand_local, hand_landmarks, frame))
                tthread_list.append(t2)
                t3 = threading.Thread(name = 't3', target = hand_coordinate, args=(hand_local, hand_landmarks, frame))
                tthread_list.append(t3)
                for tthread in tthread_list:
                    tthread.start()
                for tthread in tthread_list:
                    tthread.join()
                if hand_local:
                    angle_list = hand_angle(hand_local)
                    gesture_str = h_gesture(angle_list)
                    mouse_control(gesture_str, [hand_landmarks.landmark[9].x,hand_landmarks.landmark[9].y])
                    cv2.putText(frame,gesture_str,(0,100),0,1.3,(0,0,255),3)
        cv2.imshow('MediaPipe Hands', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cv2.destroyAllWindows()
    cap.release()

def detect_hand(frame):
    if len(frame) != 0:
        mp_drawing = mp.solutions.drawing_utils
        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands(
                static_image_mode=False,
                max_num_hands=1,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)   #改变颜色空间
        frame= cv2.flip(frame,1)              #图片水平镜像翻转
        results = hands.process(frame)        #检测手
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)   #转换回去
        gesture_str = None
        if results.multi_hand_landmarks:    #检测到手
            for hand_landmarks in results.multi_hand_landmarks:      
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)   #绘制图像
                hand_local = [0] * 22      
                tthread_list = []
                t1 = threading.Thread(name = 't1', target = hand_coordinate, args=(hand_local, hand_landmarks, frame))
                tthread_list.append(t1)
                t2 = threading.Thread(name = 't2', target = hand_coordinate, args=(hand_local, hand_landmarks, frame))
                tthread_list.append(t2)
                t3 = threading.Thread(name = 't3', target = hand_coordinate, args=(hand_local, hand_landmarks, frame))
                tthread_list.append(t3)
                for tthread in tthread_list:
                    tthread.start()
                for tthread in tthread_list:
                    tthread.join()
                if hand_local:
                    angle_list = hand_angle(hand_local)
                    gesture_str = h_gesture(angle_list)
        return gesture_str