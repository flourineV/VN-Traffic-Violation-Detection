from ultralytics import YOLO
import cv2

def detect_objects(frame, model_path='model/yolov10.pt'):
    #Load YOLO model
    model = YOLO(model_path)

    #Detect objects
    results = model.predict(frame)

    #Vẽ bounding box
    for result in results:
        for box in result.boxes:
            x1,y1,x2,y2 = map(int, box.xyxy[0])
            conf = box.conf[0]
            cls = int(box.cls[0]) 

            #vẽ box lên frame
            label = f"Class {cls}: {conf:.2f}"
            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.putText(frame,label,(x1,y1-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)

    return frame
