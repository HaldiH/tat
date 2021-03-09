import sys
import os

sys.path.append(os.getcwd() + "..")

from api import App

if __name__ == "__main__":
    # compute_files("source/image_slice_0001.png", "test")
    # image = Image.open("source/image_slice_0001.png")
    # compute_image(np.asarray(image), 4, 50, 1000)
    app = App("source_samples", "outputs")
    app.generate(4, 50, 1000)
