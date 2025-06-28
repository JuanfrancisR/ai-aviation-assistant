# Placeholder: in future, add logic to extract diagrams from PDF IPCs
# For now, use pre-saved images in /data/diagrams
def get_diagram_paths():
    import os
    base = "data/diagrams"
    return [os.path.join(base, f) for f in os.listdir(base) if f.endswith((".jpg", ".png"))]
