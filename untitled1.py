from PIL import Image
import face_recognition
image = face_recognition.load_image_file("A.jpg")
face_locations = face_recognition.face_location(image)
print("I Found {} face s in this Photograph." .format(len(face_locations)))
for face_location in face_locations:
    top,right,bottom,left = face_location
    print("A face is Located top{} , right{} , bottom{}, left{}" .format(top,left, bottom, right))
    face_image= image[top:bottom, left:right]
    pil_image=Image.fromarray(face_image)
    pil_image.show()
import numpy as np
import cv2
from matplotlib import pyplot as plt

face_cascade= cv2.cascadeClassifier("")
eye_cascade = cv2.CascadeClassifier("")

img = cv2.imread("")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detecMultiScale(gray, 1,2,3)
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y),(x+w, y+h),(255,0,0),2)
    roi_gray = gray[y:y+h , x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMutiScale(roi_gray)
    for(ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey), (ex+ew,ey+eh), (0,255,0),2)
    cv2.imshow("",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()