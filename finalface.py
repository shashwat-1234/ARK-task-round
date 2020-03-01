import cv2
from matplotlib import pyplot as plt
#trained cascade for frontal face obtained from github
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
#videocam opening
cap = cv2.VideoCapture(0) 
#camera opwn always
while 1:  
  
	# reads frames from a camera 
	ret, image = cap.read()  
  
	# convert to gray scale of each frames 
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
	cv2.waitKey(200)
	# Detects faces of different sizes in the input image 
	faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
	print(face_cascade)
	for (x,y,w,h) in faces: 
		# To draw a rectangle in a face  
		cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)  
		roi_gray = gray[y:y+h, x:x+w] 
		roi_color = image[y:y+h, x:x+w] 
		#roi is the region of interest   
	# Display an image in a window 
	cv2.imshow('facedetect',image)
	cv2.waitKey(100) 
  
# Close the window 
cap.release() 
  
# De-allocate any associated memory usage 
cv2.destroyAllWindows() 