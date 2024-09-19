import cv2
import numpy as np


def detect_shapes_in_video_agnostic(video_path):
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

        # Convert the frame to grayscale for edge detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(gray, (1, 1), 0)

        # Use Canny edge detection to detect edges in the image
        edges = cv2.Canny(blurred, 30, 130)

        # Apply morphological operations to clean up the edges
        kernel = np.ones((3, 3), np.uint8)
        edges_cleaned = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

        # Find contours based on the cleaned edges
        contours, _ = cv2.findContours(edges_cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Create a copy of the current frame for drawing
        result = frame.copy()

        # Process each contour
        for contour in contours:
            # Filter small contours to remove noise
            if cv2.contourArea(contour) < 1500:
                continue

            # Approximate the contour to reduce the number of points
            epsilon = 0.02 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            # Draw the contour on the frame
            cv2.drawContours(result, [approx], 0, (0, 255, 0), 2)

            # Calculate the center of the contour using moments
            M = cv2.moments(approx)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

                # Mark the center on the frame
                cv2.circle(result, (cX, cY), 5, (255, 0, 0), -1)

        # Display the frame with detected shapes
        cv2.imshow("Detected Shapes", result)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close windows
    cap.release()
    cv2.destroyAllWindows()


detect_shapes_in_video_agnostic("PennAir 2024 App Dynamic Hard.mp4")
