import cv2
import time

cv2.namedWindow("RTSP View", cv2.WINDOW_NORMAL)
cap = cv2.VideoCapture("rtsp://192.168.1.12:8554/video_stream")

prev_time = 0
while True:
    ret, frame = cap.read()
    if ret:
        cur_time = time.time()
        fps = 1 / (cur_time - prev_time)
        prev_time = cur_time
        
        label = "FPS: %.2f" % fps
        cv2.putText(frame, label, (15, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        cv2.imshow("RTSP View", frame)
        cv2.waitKey(1)
    else:
        print("unable to open camera")
        break

cap.release()
cv2.destroyAllWindows()
