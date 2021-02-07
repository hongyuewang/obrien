import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

webcam_capture = cv2.VideoCapture(0)

while True:
    _, img = webcam_capture.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("O'brien Facial Detection System", img)

    key = cv2.waitKey(30) & 0xff
    if key == 27:
        break

webcam_capture.release()
