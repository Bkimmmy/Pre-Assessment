# Gait Feature Extraction Tool

This tool utilizes Python, OpenCV, and MediaPipe to preprocess video data and extract key gait-related features, including **Arm Reach**, **Cadence**, **Object Detection**, and **Area Size**. The extracted features are saved in a CSV file for further analysis or machine learning applications.

## Features Extracted:
- **Arm Reach**: Measures the distance between the shoulder and wrist using MediaPipe Pose Estimation.
- **Cadence**: Estimates the cadence based on frame count and footfall detection.
- **Objects**: Detects the number of moving objects in the video using background subtraction.
- **Area Size**: Calculates the area size of the largest detected object.

## Prerequisites:
Before running the tool, ensure that you have the following installed:

- Python 3.x
- OpenCV
- MediaPipe
- NumPy
- Pandas

You can install the required packages by running the necessary commands through your terminal or command prompt to install OpenCV, MediaPipe, NumPy, and Pandas.

## Video Download Instructions:
To download a video from YouTube, you will need the `youtube-dl` tool. Install the tool by following the installation instructions provided in the official documentation. After installation, download your video by specifying the file path and video URL as required.

Replace the actual link with the YouTube video URL you want to download and ensure the video is saved in `.mp4` format for processing.

## Usage:
1. Download the video file from YouTube (as described in the video download instructions) or use your own video file.
2. Update the video path in the script to point to the location of your video file.
3. Run the tool in your Python environment to start the video processing.

## Output:
The extracted features will be saved in a CSV file named `gait_features.csv` in the same directory where the script is run. The CSV will contain the following columns:

- `Frame`: The frame number
- `Arm Reach`: The calculated distance between the shoulder and wrist
- `Cadence`: Estimated cadence based on footfall detection
- `Objects`: The number of detected moving objects
- `Area Size`: The area size of the largest detected object

### Example Output:
The output CSV might look something like this:

| Frame | Arm Reach | Cadence | Objects | Area Size  |
|-------|-----------|---------|---------|------------|
| 1     | 0.0287    |         | 1       | 2070601.0  |
| 2     | 0.0455    | 1.0     | 0       | 0.0        |

## Project Structure:
The project is structured as follows:

- `Project.py`: The main script for video preprocessing and feature extraction
- `gait_features.csv`: The output file containing the extracted features
- `README.md`: This readme file

## Notes:
- This tool is designed to extract gait features from videos with human subjects. It can be modified and refined for specific use cases, such as focusing on anomalous behavior.
- For the best results, ensure your video file has proper lighting and visibility to allow accurate feature extraction.

## References:
For additional guidance and documentation, refer to the following:

- [OpenCV Documentation](https://docs.opencv.org/)
- [MediaPipe Documentation](https://google.github.io/mediapipe/)
- [YouTube-dl Documentation](https://github.com/ytdl-org/youtube-dl)
