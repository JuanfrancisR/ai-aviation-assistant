import open_clip
import torch
from PIL import Image
import numpy as np
import faiss

model, _, preprocess = open_clip.create_model_and_transforms('ViT-B-32', pretrained='laion2b_s34b_b79k')

def search_image(query_image, index_file="visual_index/faiss.index", path_file="visual_index/image_paths.txt"):
    index = faiss.read_index(index_file)
    with open(path_file, "r") as f:
        image_paths = f.read().splitlines()

    image = preprocess(Image.open(query_image)).unsqueeze(0)
    with torch.no_grad():
        embedding = model.encode_image(image).detach().cpu().numpy().astype('float32')

    D, I = index.search(embedding, k=1)
    match_idx = I[0][0]
    return image_paths[match_idx]
