import cv2
import json

VIDEO_FILE = "tiktok_video.mp4"

# Bumping resolution back up for a sharper video!
WIDTH = 128
HEIGHT = 128

# Skip every 2nd frame to keep file size lightweight
FRAME_SKIP = 2 

cap = cv2.VideoCapture(VIDEO_FILE)
frames = []
frame_count = 0

print("Converting video with high quality settings...")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_count += 1
    if frame_count % FRAME_SKIP != 0:
        continue
    
    resized = cv2.resize(frame, (WIDTH, HEIGHT))
    
    pixel_list = []
    for row in resized:
        for b, g, r in row:
            pixel_list.extend([int(r), int(g), int(b)])
            
    frames.append(pixel_list)

cap.release()

output_data = {
    "width": WIDTH,
    "height": HEIGHT,
    "fps": 12, # Smooth target frame rate
    "frames": frames
}

with open("video1.json", "w") as f:
    json.dump(output_data, f)

print(f"Done! Created crisp video1.json with {len(frames)} frames.")
