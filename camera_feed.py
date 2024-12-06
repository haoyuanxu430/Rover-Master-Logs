import cv2
from ultralytics import YOLO
from ultralytics.engine.results import Results

from pathlib import Path
CWD = Path(__file__).parent

# Load the YOLO model
model = YOLO(CWD / "yolo11n.pt")

# Open the default camera
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Process each frame
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Run YOLO model on the frame
    results: list[Results] = model(frame)  # Perform detection on the frame

    # Print object details (bounding boxes and labels) for each detected object
    for result in results:
        for box in result.boxes:
            # Extract bounding box coordinates and label
            x1, y1, x2, y2 = box.xyxy[0]  # Bounding box coordinates
            confidence = box.conf[0]      # Confidence score
            label = result.names[box.cls[0].item()]  # Object label

            # Print information
            print(f"Detected {label} at ({x1:.0f}, {y1:.0f}, {x2:.0f}, {y2:.0f}) with confidence {confidence:.2f}")

    # Draw bounding boxes and labels on the frame
    annotated_frame = results[0].plot()  # YOLO provides an annotated frame with bounding boxes

    # Display the annotated frame
    cv2.imshow("Real-Time YOLO Detection", annotated_frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
