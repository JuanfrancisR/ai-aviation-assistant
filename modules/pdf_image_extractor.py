import fitz  # PyMuPDF
import os

def extract_images_from_pdf(pdf_path, output_folder):
    doc = fitz.open(pdf_path)
    os.makedirs(output_folder, exist_ok=True)
    count = 0

    for page_index in range(len(doc)):
        page = doc[page_index]
        images = page.get_images(full=True)
        for img_index, img in enumerate(images):
            xref = images[img_index][0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_filename = f"diagram_p{page_index+1}_{img_index+1}.{image_ext}"
            with open(os.path.join(output_folder, image_filename), "wb") as f:
                f.write(image_bytes)
            count += 1

    print(f"✅ Extracted {count} images from {pdf_path}")
    return count
