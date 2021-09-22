import cv2,imutils
cam,firstFrame = cv2.VideoCapture(0,cv2.CAP_DSHOW),None #cv2.CAP_DSHOW is written to stop the cv2 warning
while True:         #4000 is the minimum change in area
    img=imutils.resize(cam.read()[1], width=800)
    gaussianImg = cv2.GaussianBlur(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), (21, 21), 0)
    firstFrame,text =gaussianImg,"Motion Detected" if (max([cv2.contourArea(c) for c in imutils.grab_contours(cv2.findContours(cv2.dilate(cv2.threshold(cv2.absdiff(gaussianImg if firstFrame is None else firstFrame , gaussianImg), 25, 255, cv2.THRESH_BINARY)[1], None, iterations=10).copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE))]or[0])>4000) else "Normal"
    cv2.putText(img, text, (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0) if text=="Normal" else (0,0,255), 2),cv2.imshow("cameraFeed",img)
    if cv2.waitKey(1)==27:break
cam.release(),cv2.destroyAllWindows()
