import cv2
import numpy as np


def detect_shapes_in_video(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if video opened successfully
    if not cap.isOpened():
        print(f"Error: Unable to open video file {video_path}")
        return

    while True:
        # Capture each frame
        ret, frame = cap.read()

        # If the frame is not read correctly, exit the loop (end of video)
        if not ret:
            break

        # Convert to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define range for grass green color (including bright green)
        lower_green = np.array([35, 50, 50])
        upper_green = np.array([95, 255, 155])

        # Create a mask to filter out all green (grass and bright green shape)
        green_mask = cv2.inRange(hsv, lower_green, upper_green)

        # Invert the mask to keep non-green areas
        non_green_mask = cv2.bitwise_not(green_mask)

        # Apply morphological operations to remove noise
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(non_green_mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Create a copy of the current frame for drawing
        result = frame.copy()

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

        # Display the frame with detected shapes
        cv2.imshow("Detected Shapes", result)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close windows
    cap.release()
    cv2.destroyAllWindows()


detect_shapes_in_video("PennAir 2024 App Dynamic.mp4")
