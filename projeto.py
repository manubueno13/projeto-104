import cv2

receber=cv2.imread("solar-system.jpg")
print(receber)
cv2.putText(receber, "Sol",(100,80),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255))
cv2.putText(receber, "Mercurio",(100,190),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(receber, "Venus",(180,160),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(receber, "Terra",(290,170),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(receber, "Marte",(370,170),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(receber, "Jupiter",(550,50),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(receber, "Saturno.",(780,130),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(receber, "Urano",(970,140),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(receber, "Netuno",(1100,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))




cv2.imshow("sistema",receber)

cinza=cv2.cvtColor(receber,cv2.COLOR_RGB2GRAY)
print(cinza)
cv2.imshow("sistema2",cinza)

cv2.waitKey(0)

