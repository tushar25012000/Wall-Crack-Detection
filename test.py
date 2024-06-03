from ultralytics import YOLO

# loading pre-train model
model = YOLO('wallModel.pt')

# results=model(source=1,show=True,conf=0.3, save=True)
results = model(source='istockphoto-1406744517-640_adpp_is.mp4', show=True, conf=0.3, save=True)
