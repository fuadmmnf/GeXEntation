#import keyboard
import cv2
import numpy as np
import math
import os
import time
import pyautogui

from execute import execute
# from point import p_crop
# from palm import h_crop
# from fin import f_crop
# from fist import fs_crop
# from thumbdown import t_crop
# from okay import ok_crop
# from direction import dir_crop
#from finger_count import fin_count




#--------------------------------------------


os.system('ls /usr/share/applications > ../rsc/applications.txt')



# the list of applications from txt file
applicationList = list()

with open('../rsc/applications.txt') as fp:
    for line in fp:
        line = line.replace('.desktop', '')
        #print(line)
        applicationList.append(line)







# gesture detection code
cap = cv2.VideoCapture(0)
start_time = -1 
finish_time = 0
while(1):   
        isValid = False;

        _,img=cap.read()
        cv2.imshow('Webcam',img)
                
        k=cv2.waitKey(10)
        if k==27:
                break


        finish_time = time.time()
        if(start_time==-1 or finish_time-start_time>=0.5):
        
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                
                #point = point_cascade.detectMultiScale(gray,1.1,5)
                #fin=fin_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5,flags=0, minSize=(100,80))
                right_palm = right_h1_cascade.detectMultiScale(gray,1.1, 5)
                point=point_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3,flags=0, minSize=(100,80))
                #hand = hand_cascade.detectMultiScale(gray,1.1, 5)
                #LtoR=hand_left_to_right_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3,flags=0, minSize=(100,150))
                #RtoL=hand_right_to_left_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3,flags=0, minSize=(100,150))
                #finger_count = finger_count_cascade.detectMultiScale(gray,1.1,5)
                #left_palm = left_h1_cascade.detectMultiScale(gray,1.1, 5)
                #right_dir = right_cascade.detectMultiScale(gray,1.1, 5)
                #left_dir = left_cascade.detectMultiScale(gray,1.1, 5)
                fist=fist_cascade.detectMultiScale(gray,1.1, 5)
                #fist=fist_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3,flags=0, minSize=(100,150))

                thumbdown=thumbdown_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3,flags=0, minSize=(100,80))





                for (x,y,w,h) in fist:
                        print('fist')
                        start_time = time.time()
                       

                for (x,y,w,h) in right_palm:
                        print('right palm')
                        start_time = time.time()




                for (x,y,w,h) in point:
                        print('point')
                        start_time = time.time()
                

                for (x,y,w,h) in thumbdown:                    
                        print('thumbs down')
                        start_time = time.time()


                
cap.release()    
cv2.destroyAllWindows()

#----------------------------
