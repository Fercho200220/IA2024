import numpy as np
import cv2 as cv
import math 

rostro = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')
cap = cv.VideoCapture(0)
i = 0
blancos_100=0
negros_100=0
blancos_80=0
negros_80=0

while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    rostros = rostro.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in rostros:
        frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Extraer el rostro y redimensionar a 100x100
        frame2 = frame[y:y + h, x:x + w]
        frame2 = cv.resize(frame2, (100, 100), interpolation=cv.INTER_AREA)
        frame100 = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)

        # Binarizar la imagen 
        _, frame100 = cv.threshold(frame100, 127, 255, cv.THRESH_BINARY)

        blancos_100 = blancos_100 + np.sum(frame100 == 255)
        negros_100 = negros_100 + np.sum(frame100 == 0)

        cv.imwrite('C:/Users/ferco/OneDrive/Escritorio/IA/Proyecto1/imagenes/imagenes100'+str(i)+'.jpg', frame100)
        cv.imshow('Imagen 100x100', frame100)

        # Redimensionar a 80x80
        frame2 = cv.resize(frame2, (80, 80), interpolation=cv.INTER_AREA)
        frame80 = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)

        # Binarizar la imagen
        _, frame80 = cv.threshold(frame80, 127, 255, cv.THRESH_BINARY)

        blancos_80 =blancos_80+ np.sum(frame80 == 255)
        negros_80 = negros_80+np.sum(frame80 == 0)

        cv.imwrite('C:/Users/ferco/OneDrive/Escritorio/IA/Proyecto1/imagenes/imagenes80'+str(i)+'.jpg', frame80)
        cv.imshow('Imagen 80x80', frame80)
    
    cv.imshow('Rostros', frame)
    i = i + 1
    k = cv.waitKey(1)
    if k == 27:  # Presiona ESC para salir
        break

porcentajeblancos100=(blancos_100/(blancos_100+negros_100))*100
porcentajenegors100=(negros_100/(blancos_100+negros_100))*100

proporcionblancos=(blancos_100/blancos_80)
proporcionnegros=(negros_100/negros_80)

print(proporcionblancos)
print(proporcionnegros)

cap.release()
cv.destroyAllWindows()
