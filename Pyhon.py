import cv2
import json

video_path = "tiktok_video.mp4"
cap = cv2.VideoCapture(video_path)

frames_data = []
# Keep resolution low (e.g. 64x64 or 128x128) to prevent Roblox network lag
TARGET_WIDTH = 64
TARGET_HEIGHT = 64

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame
    resized = cv2.resize(frame, (TARGET_WIDTH, TARGET_HEIGHT))

    # Extract RGB values
    pixels = []
    for row in resized:
        for pixel in row:
            b, g, r = pixel
            pixels.extend([r, g, b, 255])  # RGBA

    frames_data.append(pixels)

cap.release()

# Save JSON file to host on GitHub / Server
with open("video_frames.json", "w") as f:
    json.dump({"width": TARGET_WIDTH, "height": TARGET_HEIGHT, "frames": frames_data}, f)

print("Video converted successfully!")