#impoting necessary liberaries
import cv2


#importing cascaing of face,eyes and smile
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade=cv2.CascadeClassifier('haarcascade_smile.xml')


#building function for detecting face,eyes and smile.
def detect(gray,frame):
    face=face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray,1.1,22)
        smile=smile_cascade.detectMultiScale(roi_gray,1.7,22)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        for(sx,sy,sw,sh) in smile:
            cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)
    return frame


#builiding for web cam
video_capture=cv2.VideoCapture(0)
while True:
    _,frame=video_capture.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canvas=detect(gray,frame)
    cv2.imshow('video',canvas)
    
    if(cv2.waitKey(1)&0xff==ord('q')):
        break
video_capture.release()
cv2.destroyAllWindows()
    
