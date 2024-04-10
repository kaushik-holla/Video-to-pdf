from PIL import Image

def images_to_pdf(frames, pdf_path):
    images = [Image.open(frame).convert('RGB') for frame in frames]
    images[0].save(pdf_path, save_all=True, append_images=images[1:])