import pandas as pt
import numpy as np
import os
import cv2

def save_significant_frame(video = 'video.mp4', folder_name = 'extracted_frames', threshold = 0.005):
    ## Empty list to save and compare frames
    frame_diffs = []
    saved_frames = []
    

    ## Reading the video
    vidcap = cv2.VideoCapture(video)
    
    ## Path for saving the extracted frames
    saved_path = folder_name
    os.makedirs(saved_path, exist_ok = True)

    ## Assigning success to run the loop
    success, prev_frame = vidcap.read()
    if not success:
        print("Failed to open video file or video file is empty.")

    # Convert the first frame to grayscale
    prev_frame_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    
    ## Saving the first frame
    cv2.imwrite(saved_path + '/frame_0.jpg', prev_frame)

    ## Initializing the first frame
    frame_count = 0

    ## Finding the significant frames
    while success:
        # Read next frame
        success, curr_frame = vidcap.read()
        # Exit at the end of the video
        if not success:
            break

        ## Converting the current frame to grayscale
        curr_frame_gray = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)

        ## Calculating the absolute difference between current and previous frame
        diff = cv2.absdiff(curr_frame_gray, prev_frame_gray)
        non_zero_count = np.sum(diff > 25)  # Count of pixels with difference > 25

        ## If significant difference is found, save the frame
        if (non_zero_count / diff.size) > threshold:
            saved_frame_path = f"{saved_path}/frame_{frame_count}.jpg"
            cv2.imwrite(saved_frame_path, curr_frame)
            saved_frames.append(saved_frame_path)
            prev_frame_gray = curr_frame_gray # Update the previous frame

        frame_count += 1

    ## Clean up and release the video
    vidcap.release()

    return saved_frames
