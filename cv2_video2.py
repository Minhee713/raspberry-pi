import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter('output.avi', fourcc, fps, (w,h))

while cap.isOpened():
    ret, img = cap.read()

    if ret:
        cv2.imshow('Video Capture', img)

        out.write(img)

        k = cv2.waitKey(1) &0xFF 
        if k == 27:
            break

out.release()
cap.release()
cv2.destroyAllWindows()
