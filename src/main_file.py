#import keyboard
import cv2
import numpy as np
import math
import os
import time
import pyautogui
# from point import p_crop
# from palm import h_crop
# from fin import f_crop
# from fist import fs_crop
# from thumbdown import t_crop
# from okay import ok_crop
# from direction import dir_crop

#os.chdir("/home/gesentation/src/haarCascades")
right_h1_cascade=cv2.CascadeClassifier('./haarCascades/rpalm.xml') # right palm
#hand_cascade = cv2.CascadeClassifier('heppu_handa.xml')
#left_h1_cascade=cv2.CascadeClassifier('lpalm.xml') #left palm
#right_cascade=cv2.CascadeClassifier('right.xml') #right direction
#left_cascade=cv2.CascadeClassifier('left.xml') #left direction
#finger_count_cascade = cv2.CascadeClassifier('finger_count.xml')
#okay_cascade = cv2.CascadeClassifier('ok.xml') # okay sign
#point_cascade = cv2.CascadeClassifier('point1.xml')
#fin_cascade=cv2.CascadeClassifier('fin_2.xml') 
hand_left_to_right_cascade = cv2.CascadeClassifier('./haarCascades/heppu_handb.xml')
hand_right_to_left_cascade = cv2.CascadeClassifier('./haarCascades/heppu_hands.xml')
#fist_cascade=cv2.CascadeClassifier('aGest.xml') # fist
#thumbdown_cascade = cv2.CascadeClassifier('thumbdown.xml')
cap = cv2.VideoCapture(0)
ca=0
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
        if(start_time==-1 or finish_time-start_time>=0.3):
        
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                #point=point_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3,flags=0, minSize=(100,80))
                #fin=fin_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5,flags=0, minSize=(100,80))
                right_palm = right_h1_cascade.detectMultiScale(gray,1.1, 5)
                #hand = hand_cascade.detectMultiScale(gray,1.1, 5)
                LtoR = hand_left_to_right_cascade.detectMultiScale(gray, 1.1, 5)
                RtoL = hand_right_to_left_cascade.detectMultiScale(gray, 1.1, 5)
                #finger_count = finger_count_cascade.detectMultiScale(gray,1.1,5)
                #left_palm = left_h1_cascade.detectMultiScale(gray,1.1, 5)
                #right_dir = right_cascade.detectMultiScale(gray,1.1, 5)
                #left_dir = left_cascade.detectMultiScale(gray,1.1, 5)
                #fist=fist_cascade.detectMultiScale(gray,1.3, 5)
                #okay=okay_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3,flags=0, minSize=(100,150))
                #thumbdown=thumbdown_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3,flags=0, minSize=(100,80))

                #print(len(finger_count)/4)
                # for (x,y,w,h) in left_palm:
                #         #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                #         roi_gray=gray[y:y+h,x:x+w]
                #         roi_color=img[y:y+h,x:x+w]
                #         crop_img=img[y:y+h,x:x+w]
                #         h_crop(crop_img,img,'left')
                #         start_time = time.time()
                #         isValid = True;



                # for (x,y,w,h) in fist:
                #         #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                #         # roi_gray = gray[y:y+h,x:x+w]
                #         # roi_color = img[y:y+h,x:x+w]
                #         # crop_img = img[y:y+h,x:x+w]
                #         # fs_crop(crop_img,img)
                #         isValid = True
                #         print('fist')
                #         start_time = time.time()
                       

                # for (x,y,w,h) in hand:
                #         #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                #         # roi_gray = gray[y:y+h,x:x+w]
                #         # roi_color = img[y:y+h,x:x+w]
                #         # crop_img = img[y:y+h,x:x+w]
                #         # fs_crop(crop_img,img)
                #         print('hand found')
                #         isValid = True
                #         start_time = time.time()
                       
                for (x,y,w,h) in right_palm:
                        #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                        # roi_gray=gray[y:y+h,x:x+w]
                        # roi_color=img[y:y+h,x:x+w]
                        # crop_img=img[y:y+h,x:x+w]
                        # h_crop(crop_img,img, 'right')
                        isValid = True
                        print('right palm')
                        start_time = time.time()

               
                # print('')
                if isValid:
                        # for (x,y,w,h) in RtoL:
                        #         #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                        #         # roi_gray=gray[y:y+h,x:x+w]
                        #         # roi_color=img[y:y+h,x:x+w]
                        #         # crop_img=img[y:y+h,x:x+w]
                        #         # h_crop(crop_img,img, 'right')
                        #         print('right swipe')
                        #         start_time = time.time()

                        for (x,y,w,h) in LtoR:
                                #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                                # roi_gray=gray[y:y+h,x:x+w]
                                # roi_color=img[y:y+h,x:x+w]
                                # crop_img=img[y:y+h,x:x+w]
                                # h_crop(crop_img,img, 'right')
                                #if isValid:
                                print('left swipe')
                                start_time = time.time()


                # for (x,y,w,h) in right_dir:
                #         #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                #         roi_gray=gray[y:y+h,x:x+w]
                #         roi_color=img[y:y+h,x:x+w]
                #         crop_img=img[y:y+h,x:x+w]
                #         dir_crop(crop_img,img, 'right')
                #         start_time = time.time()


                # for (x,y,w,h) in left_dir:
                #         #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                #         print('aise ekhan')
                #         roi_gray=gray[y:y+h,x:x+w]
                #         roi_color=img[y:y+h,x:x+w]
                #         crop_img=img[y:y+h,x:x+w]
                #         dir_crop(crop_img,img, 'left')
                #         start_time = time.time()





                # for (x,y,w,h) in fin:
                #         # cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
                #         # roi_gray=gray[y:y+h,x:x+w]
                #         # roi_color=img[y:y+h,x:x+w]
                #         # crop_img=img[y:y+h,x:x+w]
                #         # f_crop(crop_img,img)
                #         print('victory')
                #         start_time = time.time() 
                #         #time.sleep(0.5)





                # for (x,y,w,h) in okay:
                #         #cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                #         roi_gray=gray[y:y+h,x:x+w]
                #         roi_color=img[y:y+h,x:x+w]
                #         crop_img=img[y:y+h,x:x+w]
                #         ok_crop(crop_img,img)
                #         start_time = time.time()
                #         #time.sleep(0.5)
                        
                        
                # for (x,y,w,h) in point:
                #         cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
                #         roi_gray=gray[y:y+h,x:x+w]
                #         roi_color=img[y:y+h,x:x+w]
                #         crop_img=img[y:y+h,x:x+w]
                #         ha=2
                #         p_crop(crop_img,img)
                #         #time.sleep(0.5)

                

                # for (x,y,w,h) in thumbdown:
                #         cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                #         roi_gray=gray[y:y+h,x:x+w]
                #         roi_color=img[y:y+h,x:x+w]
                #         crop_img=img[y:y+h,x:x+w]
                #         ha=5
                #         t_crop(crop_img,img)
                #         #time.sleep(0.5)

                

                
        
cv2.destroyAllWindows()

    
