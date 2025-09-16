from ultralytics import YOLO
import os
from PIL import Image
from statistics import mean

model = YOLO('yolov8n.pt')
model.to('cpu')

# Folder with images
# image_folder = r"D:\Document\University\CS231\CS231_project\dataset\test_b\data"
# image_folder = r"D:\Document\University\CS231\CS231_project\test\baseline"
image_folder = r"D:\Document\University\CS231\CS231_project\test\dsconv"


image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]

# Metrics
main_confidences = []
object_counts = []


for img_file in image_files:
    img_path = os.path.join(image_folder, img_file)
    results = model(img_path)
    detections = results[0].boxes
    
    if detections:
        scores = [float(box.conf[0]) for box in detections]
        main_confidences.append(max(scores))
        object_counts.append(len(detections))
    # else:
        # main_confidences.append(0.0)
        # object_counts.append(0)


print(f"Processed {len(image_files)} images")
print(f"Average main object confidence: {mean(main_confidences):.2f}")
print(f"Average number of objects: {sum(object_counts):.2f}")

