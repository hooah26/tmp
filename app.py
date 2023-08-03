import sys
import cv2
import imutils
from yoloDet import YoloTRT

# use path for library and engine file
model = YoloTRT(library="yolov7/build/libmyplugins.so", engine="yolov7/build/yolov7-tiny.engine", conf=0.5, yolo_ver="v7")

# Use the default camera connected to the system
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=600)
    detections, t = model.Inference(frame)

    # Calculate FPS
    fps = 1 / t
    fps_text = "FPS: {:.2f}".format(fps)

    # Filter and draw only human detections
    for obj in detections:
        print(ojb)
        if obj['class'] == 'person': # Assuming the human class is labeled as 'person'
            conf = obj['conf']
            box = obj['box']
            x, y, w, h = box
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "Person: {:.2f}".format(conf), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display FPS on the frame
    cv2.putText(frame, fps_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Output", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
