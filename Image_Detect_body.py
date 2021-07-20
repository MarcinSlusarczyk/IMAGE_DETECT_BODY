import cv2
face_cascade = cv2.CascadeClassifier(f'D:\\Users\\marci\\AppData\\Local\\Programs\\Python\\Python39\\PYTHON PROJECTS\\OpenCV\\haarcascade_fullbody.xml') #location training model xml
img = cv2.imread(f'C:\\Users\\marci\\Downloads\\auta.jpg') #location image 

while True:

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 1)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('fota', img)
    cv2.waitKey(2)
