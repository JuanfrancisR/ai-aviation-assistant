import open_clip
import torch
from PIL import Image
import os
import numpy as np
import faiss

# Load CLIP model
model, _, preprocess = open_clip.create_model_and_transforms('ViT-B-32', pretrained='laion2b_s34b_b79k')
tokenizer = open_clip.get_tokenizer('ViT-B-32')

def build_image_index(image_folder, index_file="visual_index/faiss.index"):
    image_paths = []
    embeddings = []

    for fname in os.listdir(image_folder):
        if fname.lower().endswith((".jpg", ".png")):
            path = os.path.join(image_folder, fname)
            image = preprocess(Image.open(path)).unsqueeze(0)
            with torch.no_grad():
                embedding = model.encode_image(image).detach().cpu().numpy().flatten()
                embeddings.append(embedding)
                image_paths.append(fname)

    vectors = np.vstack(embeddings).astype('float32')
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)

    os.makedirs("visual_index", exist_ok=True)
    faiss.write_index(index, index_file)

    # Save image paths
    with open("visual_index/image_paths.txt", "w") as f:
        f.write("\n".join(image_paths))

    return index_file
