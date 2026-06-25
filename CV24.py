import cv2

# Read the main image and watermark image
img = cv2.imread("C:/Users/vanib/Downloads/download (2).jpg")
wm = cv2.imread("C:/Users/vanib/Downloads/download (1).jpg")

# Resize images
resized_img = cv2.resize(img, (600, 400))
resized_wm = cv2.resize(wm, (150, 100))

# Get dimensions
h_img, w_img, _ = resized_img.shape
center_y = int(h_img / 2)
center_x = int(w_img / 2)

h_wm, w_wm, _ = resized_wm.shape

# Calculate position for watermark at center
top_y = center_y - int(h_wm / 2)
left_x = center_x - int(w_wm / 2)
bottom_y = top_y + h_wm
right_x = left_x + w_wm

# Region of interest
roi = resized_img[top_y:bottom_y, left_x:right_x]

# Blend watermark with image
result = cv2.addWeighted(roi, 1, resized_wm, 0.3, 0)

# Replace ROI with blended result
resized_img[top_y:bottom_y, left_x:right_x] = result

# Save output image
filename = "C:/Users/vanib/Downloads/output_watermark.jpg"
cv2.imwrite(filename, resized_img)

# Display image
cv2.imshow("Watermarked Image", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
