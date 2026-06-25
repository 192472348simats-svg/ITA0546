import cv2
import numpy as np

# Read image
image = cv2.imread("C:/Users/vanib/Downloads/Captain America Hd image - Wallpaper.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw rectangles around detected objects
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)

    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Extract object
    extracted_object = image[y:y+h, x:x+w]

    # Resize extracted object for better viewing
    extracted_object = cv2.resize(extracted_object, (400, 400))

    cv2.imshow("Extracted Object", extracted_object)
    cv2.waitKey(0)

# Resize final image for display
display_image = cv2.resize(image, (1000, 700))

cv2.imshow("Objects with Rectangles", display_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
