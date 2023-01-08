import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while True:
  ret, frame = cap.read()
  width = int(cap.get(3)) #For width
  height = int(cap.get(4)) #For Height

  image = np.zeros(frame.shape, np.uint8) #Only blank image
  smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5) #Cutting the hight and width dimension in half
  image[:height//2, :width//2] = smaller_frame #Top Left
  image[height//2:, :width//2] = smaller_frame #Bottom Left
  image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180) #Top right
  image[height//2:, width//2:] = smaller_frame #Bottom Right


  cv2.imshow('frame', image) 
  
  if cv2.waitKey(1) == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
