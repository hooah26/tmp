import sys
import cv2
import imutils
from yoloDet import YoloTRT

# use path for library and engine file
model = YoloTRT(library="yolov5/build/libmyplugins.so", engine="yolov5/build/yolov5s.engine", conf=0.5, yolo_ver="v5")

# Use the default camera connected to the system
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=600)
    detections, t = model.Inference(frame)

    # Calculate FPS
    fps = 1 / t
    fps_text = "FPS: {:.2f}".format(fps)

    # Iterate over the detections and only consider those with class ID for people (typically 0 for COCO)
    for obj in detections:
        if obj['class'] == 0: # assuming class ID for 'person' is 0
            box = obj['box']
            x, y, w, h = map(int, box)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Add more code here if you want to do something specific with the detected people

    # Display FPS on the frame
    cv2.putText(frame, fps_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Output", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
