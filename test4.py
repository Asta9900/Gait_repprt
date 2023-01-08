import numpy as np
import cv2
import requests

url="https://192.168.210.249:8080/shot.jpg"
while True:
  #ret, frame = cap.read()
  mob_cam = requests.get(url, verify=False)
  image_arr = np.array(bytearray(mob_cam.content), dtype=np.uint8)
  frame = cv2.imdecode(image_arr, -1)
  #displaying frame on screen
  cv2.imshow('window', frame)

  if cv2.waitKey(1) == ord('q'):
    break   #Use 'q' to exit

#cap.release()
cv2.destroyAllWindows()
