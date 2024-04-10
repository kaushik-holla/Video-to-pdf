# Video Notes Creator
This project provides a Python solution for automatically extracting significant frames from a video file and compiling them into a single PDF document. It's particularly useful for creating visual notes from educational videos, presentations, or any video content where key frames capture essential information. The tool analyzes each frame of a video, identifies frames with significant changes, and compiles these frames into a PDF, effectively turning a video into an easily reviewable document.

## Features
<b>Frame Extraction:</b> Automatically detects and extracts frames with significant visual changes from a video, reducing the content to its most informative parts. <br>
<b>PDF Compilation:</b> Converts the extracted frames into a single PDF document, making it easy to review and study the video content in a static, portable format. <br>
<b>Customizable Sensitivity:</b> Offers the ability to adjust the sensitivity of change detection to capture more or fewer frames based on the specific content of the video.<br>

## Prerequisites
Before running this tool, ensure you have the following libraries installed in your Python environment:

opencv-python-headless: For video processing and frame extraction.<br>
Pillow (PIL Fork): For image manipulation and compiling images into a PDF.<br>

You can install these dependencies via pip

## Usage

<b>Frame Extraction:</b><br>
The script frame_extractor.py is responsible for analyzing the video and extracting frames where significant changes occur.
It compares consecutive frames, calculating the difference, and saves those frames that surpass a specified threshold of change.

<b>Images to PDF:</b><br>
The script images_to_pdf.py takes the extracted frames and compiles them into a single PDF document.
The PDF document will be saved in the specified output directory, ready for review.
To use this tool, run the main script (assuming main.py), providing the path to your video file. The script will then process the video and output the PDF to your chosen location.

<b>Configuration:</b><br>
Threshold Adjustment: You can adjust the sensitivity of the frame extraction by modifying the threshold parameter in frame_extractor.py. Lowering the threshold captures more frames, while increasing it results in fewer, more significant changes being captured.

<b>Output Directory:</b><br>
Specify your desired output directory for the PDF in the script. Ensure this directory exists or that the script has permission to create it.

## Contributing
Contributions to improve the tool are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

## Acknowledgments
This project uses OpenCV and PIL, powerful libraries for image processing and manipulation. Thanks to the developers and contributors of these libraries.
