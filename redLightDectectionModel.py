import os
import torch
from ultralytics import YOLOv10


if __name__ == "__main__":
    train_path = './yolo_traffic_light_dataset/dataset.yaml'

    # Load a model
    model = YOLOv10("yolov8n.pt")  # load pre trained model

    # Use the model
    model.train(data=train_path, epochs=100, batch=1)  # train the model


