import cv2
import numpy as np

def templateMatch():
    '''
    finding the landing pad in a frame
    knowing the depth from camera to ground/object
    will make this method better with a resizing method

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
        template = resizing(template,1,1) #not resizing right now
        h, w= template.shape[0:2]

        # all template matching methods in openCV library: [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED
        # , cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
        #best methods: [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED]


        img2 = frame.copy()

        #display matches
        method =cv2.TM_CCOEFF_NORMED
        result = cv2.matchTemplate(img2,template,method)

        min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc


        if((method in [cv2.TM_CCOEFF_NORMED,cv2.TM_CCORR_NORMED,cv2.TM_SQDIFF_NORMED]) and (max_val >= 0.5)):
            #draw rectangle around the match
            bottom_right = (top_left[0] + w, top_left[1] + h)
            cv2.rectangle(img2,top_left,bottom_right,255,5)

        cv2.imshow('Match', img2)

        #wait 1 milsec
        #if key q is pressed, quit the whole process
        if(cv2.waitKey(1) == ord('q')):
            break
    camera.release()
    cv2.destroyAllWindows()



    return False

def resizing(template,focal,depth):
    '''

    formula: size in camera = actual size * focal/depth

    :param filename: template filename
    :param height: actual object height
    :param width: actual object width
    :param focal: focal length
    :param depth: distance between camera to object/ground
    :return: resized template
    '''
    ratio = focal/depth
    img = cv2.resize(template,(0,0),fx=ratio,fy=ratio)
    return img

def centerOfFrame():
    '''
    identify the center of the object to track
    :return: pixel coordinate maybe?
    '''
    return None
templateMatch()