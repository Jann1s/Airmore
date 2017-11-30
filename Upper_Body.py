import cv2
import sys

#cascPath = sys.argv[0]
bodyCascade = cv2.CascadeClassifier('haarcascade_mcs_upperbody.xml')
cap = cv2.imread('thermal.jpg', 0)

while True:
    # Capture frame-by-frame
    #ret, frame = video_capture.read()

    color = cv2.cvtColor(cap, cv2.COLOR_GRAY2BGR)
    #gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)

    body = bodyCascade.detectMultiScale(
        cap,
        scaleFactor=1.5,
        minNeighbors=1,
        minSize=(100,200),
        flags=0
    )

    count = 0

    # Draw a rectangle around the faces
    for (x, y, w, h) in body:
        cv2.rectangle(cap, (x, y), (x+w, y+h), (0, 255, 0), 2)
        count = count + 1

    print count

    cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Video', 800, 600)
    cv2.imshow('Video', cap, )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
