import numpy as np
import cv2
cap = cv2.imread('testimage.png', 0);
while(1==1):
    thresh1 = cv2.applyColorMap(cap,cv2.COLORMAP_JET)
    cv2.imshow('frame',thresh1)

    if cv2.waitKey(100)&0xFF==ord('q'):
        break

cap.release()
cv2.distroyAllWindows()
