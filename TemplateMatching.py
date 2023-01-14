import cv2
import numpy as np

def templateMatch():
    '''
    finding the landing pad in a frame

    :return: boolean
    '''

    #load camera
    #0 means first video source
    #Yijun: I have a video capture card so for me '1' is the external webcam
    camera = cv2.VideoCapture(1)
    #display camera feed
    while(True):
        #ret: boolean for if capture properly
        #frame = image captured
        ret,frame = camera.read()
        cv2.imshow('frame',frame)

        #template matching
        template = cv2.imread('testingTemplate.jpg')
        h, w= template.shape[0:2]

        # all template matching methods in openCV library: [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED
        # , cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
        #best methods: [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED]


        img2 = frame.copy()

        #display matches
        method =cv2.TM_CCORR
        result = cv2.matchTemplate(img2,template,method)
        min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc

        #draw rectangle around matches
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(img2,top_left,bottom_right,255,5)
        cv2.imshow('Match',img2)

        #wait 1 milsec
        #if key q is pressed, quit the whole process
        if(cv2.waitKey(1) == ord('q')):
            break
    camera.release()
    cv2.destroyAllWindows()



    return False

def centerOfFrame():

    return None
templateMatch()