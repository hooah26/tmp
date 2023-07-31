import cv2
import threading
import pyrealsense2 as rs
import numpy as np
import time


def camera_check():
    for i in range(5):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"Camera index {i} is available.")
            cap.release()
        else:
            print(f"Camera index {i} is not available.")


def rgb_camera(camera_index, window_name):
    cap = cv2.VideoCapture(camera_index)
    prev_frame_time = 0
    if not cap.isOpened():
        print("Error: Could not open camera with index", camera_index)
        return
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    while True:
        ret, frame = cap.read()
        if ret:
            # Calculate FPS
            new_frame_time = time.time()
            fps = 1 / (new_frame_time - prev_frame_time)
            prev_frame_time = new_frame_time

            fps_text = f'FPS: {int(fps)}'
            cv2.putText(frame, fps_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            cv2.imshow(window_name, frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyWindow(window_name)


def depth_camera():
    # Configure depth and color streams
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
    config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)

    # Start streaming
    pipeline.start(config)
    prev_frame_time = 0
    try:
        while True:
            frames = pipeline.wait_for_frames()
            depth_frame = frames.get_depth_frame()
            color_frame = frames.get_color_frame()
            if not depth_frame or not color_frame:
                continue

            depth_image = np.asanyarray(depth_frame.get_data())
            color_image = np.asanyarray(color_frame.get_data())

            # Calculate FPS
            new_frame_time = time.time()
            fps = 1 / (new_frame_time - prev_frame_time)
            prev_frame_time = new_frame_time

            fps_text = f'FPS: {int(fps)}'
            cv2.putText(color_image, fps_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)
            images = np.hstack((color_image, depth_colormap))

            cv2.imshow('RealSense', images)
            if cv2.waitKey(1) & 0xFF == ord('w'):
                break
    finally:
        # Stop streaming
        pipeline.stop()
        cv2.destroyAllWindows()


# Uncomment this line to check available cameras
# camera_check()

# Create threads for each camera
thread1 = threading.Thread(target=rgb_camera, args=(4, "RGB"))
thread2 = threading.Thread(target=depth_camera)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

cv2.destroyAllWindows()
