from ultralytics import YOLO
model = YOLO('yolov8n.pt')
model(source=r'D:\Cars Project\Project\30 Minutes of Cars Driving By in 2009_3.mp4',
      show=True, verbose=False)
