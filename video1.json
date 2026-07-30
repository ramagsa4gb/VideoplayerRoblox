import cv2
import json

VIDEO_FILE = "tiktok_video.mp4"
WIDTH, HEIGHT = 128, 128

cap = cv2.VideoCapture(VIDEO_FILE)
frames = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break
    resized = cv2.resize(frame, (WIDTH, HEIGHT))
    pixel_list = []
    for row in resized:
        for b, g, r in row:
            pixel_list.extend([int(r), int(g), int(b)])
    frames.append(pixel_list)

cap.release()

with open("video1.json", "w") as f:
    json.dump({"width": WIDTH, "height": HEIGHT, "fps": 15, "frames": frames}, f)

print("video1.json created successfully!")
