# Shape Detection Algorithm

This repository contains an algorithm to detect, trace, and locate the centers of solid shapes on various backgrounds using OpenCV. 
The solution has been applied to static images, videos, and an agnostic environment with varying backgrounds and multicolored shapes. Below is the documentation of the code, its implementation, and the results.

## Table of Contents
- [Code Implementation](#code-implementation)
- [Static Image Results](#static-image-results)
- [Video Results](#video-results)
- [Background Agnostic Results](#background-agnostic-results)
- [Running the Code](#running-the-code)
- [Additional Documentation](#additional-documentation)

## Code Implementation
For the challenge there were three "stages" of processing:
1. **Static Image Processing**: Detects shapes in a static image and marks the contours and centers.
2. **Video Processing**: Applies the shape detection algorithm to a video stream frame by frame, marking shapes in real-time.
3. **Background Agnostic Processing**: Extends the detection to work on videos with varying backgrounds/textures and multicolored shapes.

### Key Steps
1. **Preprocessing**: Each image or video frame is preprocessed using blurring and edge detection to reduce noise and enhance shape contours.
2. **Edge Detection**: the Canny edge detection algorithm is applied to detect the contours of the shapes.
3. **Contour Processing**: Contours are approximated and filtered by size to eliminate noise. The algorithm then traces the contour and computes the center of each shape.
4. **Background Agnostic Modifications**: For background-independent detection, adaptive thresholding and color masking were added to ensure shape detection in varying backgrounds and lighting conditions.

### Documentation in Code
Each function is documented to explain the key operations and logic. Comments highlight critical operations like image filtering, contour extraction, and moment calculations.

---

## Static Image Results

<img width="946" alt="Screenshot 2024-09-18 at 8 01 08 PM" src="https://github.com/user-attachments/assets/25f1cb24-8555-41a0-b20e-71be0798eb9d">

### Approach
- **Input**: A static image with solid shapes on a grassy background.
- **Process**: 
  - The image was converted to grayscale.
  - Gaussian blur was applied to reduce noise.
  - Canny edge detection identified shape boundaries.
  - Contours were extracted, and small contours were filtered out.
  - Moments were calculated to locate the center of each shape.

### Challenges
- **Noise Removal**: All of the first attempts with edge detection produced too much noise due to the textured background. Applying morphological operations like closing helped reduce this.
- **Shape Simplification**: Some contours had too many points, leading to jagged edges. Adjusting the approximation factor smoothed the shapes.

---

## Video Results

https://github.com/user-attachments/assets/ac140870-3ca1-4c4e-b057-dce79d481d21

### Approach
- **Input**: A video with solid shapes on a grassy background.
- **Process**: 
  - The same approach used for the static image was applied frame-by-frame to a video stream.
  - Contours and centers were traced in each frame, and the video was saved with the processed frames.

### Performance and Adjustments
- **Efficiency**: To process each frame in real-time, computationally expensive operations were minimized. For instance:
  - A smaller Gaussian blur kernel was used to retain more shape details.
  - Edge detection thresholds were optimized to detect relevant edges while ignoring background noise.
- **Real-time Processing**: The algorithm runs smoothly at the video's native frame rate, providing real-time shape detection and marking.

---

## Background Agnostic Results

https://github.com/user-attachments/assets/9b70ddb9-ef42-46b8-92d1-60cb0cdec3fc

### Modifications
- **Color Independence**: Adaptive thresholding was implemented to handle videos with varying backgrounds and multicolored shapes.
- **HSV Masking**: Instead of relying on a fixed color threshold, the algorithm was modified to work with shapes of any color by using the HSV color space to filter out background regions.
- **Performance**: The algorithm does not work that well, and I am currently learning more ways to improve it!

### Challenges
- **Complex Backgrounds**: Maintaining accurate detection on highly textured or multicolored backgrounds was difficult. Adjusting the edge detection thresholds and using adaptive filters helped improve the accuracy.

---

## Running the Code

To run the shape detection algorithms:

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- OpenCV (`cv2`)

Cloning the Repository
To get started, clone this repository using the following command:

```bash
Copy code
git clone https://github.com/arJ-V/PennAerial.git
cd PennAerial
```

Install OpenCV using:
```bash
pip install opencv-python opencv-python-headless
```

### Running the Static Image Detection
```bash
python detect_shapes.py
```
This will run the shape detection algorithm on the provided static image file.

### Running the Video Detection
```bash
python detect_shapes_in_video.py
```
This will process each frame of the video and will display the output video with detected shapes.

### Running the Background Agnostic Detection
```bash
python detect_shapes_in_video_agnostic.py
```
This version is designed for more complex backgrounds and will display the output video with the detected shapes.

---

## Additional Documentation

### Algorithm Explanation
- **Canny Edge Detection**: Used to identify shape boundaries.
- **Moment Calculation**: Used to compute the center of each detected shape.
- **Contour Approximation**: Reduces the complexity of the detected shape contours.
- **Morphological Operations**: Applied to clean up the edges and remove noise.

For more information on OpenCV methods used in the code, refer to the [OpenCV documentation](https://docs.opencv.org/).



