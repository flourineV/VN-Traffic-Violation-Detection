import cv2
import os

cap = cv2.VideoCapture('...')

#tạo thư mục

frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Deo access dc")
        break

    #lưu frame bằng ảnh
    cv2.imwrite(f'frames/frame_{frame_count:04d}.jpg',  frame)
    frame_count+=1

cap.release()
print(f'Total frames extracted: {frame_count}')