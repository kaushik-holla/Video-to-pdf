from save_frames import save_significant_frame
from images_to_pdf import images_to_pdf

if __name__ == '__main__':
    video = 'video.mp4'
    folder_name = 'extracted_frames'
    threshold = 0.005
    pdf_path = 'video_summary.pdf'

    saved_frames = save_significant_frame(video, folder_name, threshold)
    if saved_frames:
        images_to_pdf(saved_frames, pdf_path)
        print("PDF created successfully.")
    else:
        print("Error with PDF creation.")