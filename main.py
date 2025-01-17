import cv2
import pytesseract
import numpy as np
from ultralytics import YOLO

#YOLOV10
MODEL_PATH = 'models/yolov10.pt'

#OCR config


model = YOLO(MODEL_PATH)

def detect_realtime():
    cap = cv2.VideoCapture(0) #Camera open

    lower_range_red = np.array([0,43,184])
    upper_range_red = np.array([56,132,255])

    while True:
        ret, frame = cap.read()
        if not ret: 
            print("Cannot capture frame")
            break
        
        #phát hiện đối tượng bằng yolov10
        results = model.predict(frame,conf=0.5)
        
        stop_line_crossed = False
        license_plate_text = ""

        for result in results:
            boxes = result.boxes.data
            for box in boxes:
                x1,y1,x2,y2, confg, cls = box.tolist()
                label = result.names[int(cls)]

                #phát hiện đèn đỏ/ đèn vàng
                if label == "red_light":
                    red_light_detected = True
                    cv2.rectangle(frame,(int(x1),int(y1),int(x2),int(y2)),(0,0,255),2)
                if label == "yellow_light":
                    red_light_detected = True
                    cv2.rectangle(frame,(int(x1),int(y1),int(x2),int(y2)),(0,0,255),2)

                #phát hiện phương tiện vượt vạch (bánh trước)
                if label in ["car","motorbike", "bus"]:
                    
        
        
        #phát hiện biển số
        #liệt biển số vào mảng
    #giải phóng cam + destroy windows.
