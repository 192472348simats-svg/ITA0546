import cv2

# Load main image
main_image = cv2.imread("C:/Users/vanib/Downloads/download (2).jpg")

if main_image is not None:

    # Get dimensions of main image
    main_height, main_width, _ = main_image.shape

    # Crop a region from the top-left corner
    crop_height, crop_width = 80, 288
    cropped_region = main_image[0:crop_height, 0:crop_width]

    # Position to paste the cropped region at the bottom-right corner
    paste_x = main_width - crop_width
    paste_y = main_height - crop_height

    # Paste the cropped region
    main_image[paste_y:paste_y + crop_height,
               paste_x:paste_x + crop_width] = cropped_region

    # Display result
    cv2.imshow("Result", main_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Error: Could not load main image.")
