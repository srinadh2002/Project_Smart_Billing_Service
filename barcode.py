import cv2
import pyzbar.pyzbar as pyzbar


cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        (x,y,w,h)=obj.rect
        cv2.rectangle(frame,(x-10,y-10),(x+w+10,y+h+10),(255,0,0),2)
        k=obj.data
        print(k)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
