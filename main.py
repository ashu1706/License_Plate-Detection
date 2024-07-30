import cv2


##################################################
frameWidth = 650
frameHeight = 480
nPlateCascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")
minArea= 500
color= (255,00,255)
##################################################

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(3, frameHeight)
cap.set(30, 150)
while True:
    success, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    nPlate = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in nPlate:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img, "NumberPlate", (x,y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,1 ,color, 2)

            imgRoi= img[y:y+h, x:x+w]
            cv2.imshow("ROI",imgRoi)

    cv2.imshow("result", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
          break

