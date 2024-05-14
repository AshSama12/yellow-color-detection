import cv2
from PIL import Image

from util import get_limits

# Define the lower and upper HSV limits for yellow color
yellow_lower = (20, 100, 100)
yellow_upper = (30, 255, 255)

cap = cv2.VideoCapture(0)  # Assuming webcam is at index 0
if not cap.isOpened():
    print("Error: Unable to open webcam.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Unable to capture frame.")
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image to get only yellow colors
    mask = cv2.inRange(hsvImage, yellow_lower, yellow_upper)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    print(bbox)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
