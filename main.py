import cv2
import numpy as np


def detect_shapes(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define range for grass green color (including bright green)
    lower_green = np.array([35, 50, 50])
    upper_green = np.array([95, 255, 155])

    # Create a mask to filter out all green (including grass and bright green shape)
    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    # Invert the mask to keep non-green areas
    non_green_mask = cv2.bitwise_not(green_mask)

    # Apply morphological operations to remove noise
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(non_green_mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a copy of the original image for drawing
    result = image.copy()

    # Process each contour
    for contour in contours:
        # Filter small contours
        if cv2.contourArea(contour) < 500:
            continue

        # Approximate the contour to reduce the number of points
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Draw the contour
        cv2.drawContours(result, [approx], 0, (0, 255, 0), 2)

        # Calculate the center of the contour
        M = cv2.moments(approx)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            # Mark the center
            cv2.circle(result, (cX, cY), 5, (255, 0, 0), -1)

    # Display the result
    cv2.imshow("Detected Shapes", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect_shapes("PennAir 2024 App Static.png")