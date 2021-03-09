import matplotlib.pyplot as plt
import numpy as np
from skimage import filters
from sklearn.cluster import KMeans
from PIL import Image
import os
import time
import mimetypes


def compute_image(src_image, cluster_count, run_count, max_iter_count):
    img_shape = src_image.shape
    start_time = time.time()
    k_means = KMeans(n_clusters=cluster_count, random_state=0, n_init=run_count, max_iter=max_iter_count).fit(
        filters.gaussian(src_image.reshape(img_shape[0] * img_shape[1], 1), 2))
    delta = time.time() - start_time
    print(f"k-means computing time: {delta}")
    segments = k_means.labels_.reshape(img_shape)
    labeled_segments = k_means.cluster_centers_[segments][:, :, 0]
    labeled_cluster = np.asarray(k_means.cluster_centers_)

    powers = np.floor(np.log10(labeled_segments))
    monochrome_labeled_segments = 100 ** powers * np.floor(labeled_segments / 100 ** powers)

    powers_cluster = np.floor(np.log10(labeled_cluster))
    monochrome_labeled_cluster = np.sort(100 ** powers_cluster * np.floor(labeled_cluster / 100 ** powers_cluster),
                                         axis=0)

    layers = []
    for i in range(len(monochrome_labeled_cluster)):
        layer = np.zeros(shape=np.shape(monochrome_labeled_segments))
        layer[monochrome_labeled_segments == monochrome_labeled_cluster[i]] = 1
        layers.append(layer)
    return layers


def guess_type(filename):
    return mimetypes.guess_type(filename)[0].split("/")[0]


def is_image(filename):
    return guess_type(filename) == "image"


class App:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder

    def generate(self, cluster_count, run_count, max_iter_count):
        for entry in os.scandir(self.input_folder):
            if not is_image(entry.path):
                continue

            image = Image.open(entry.path)
            input_basename = (lambda basename: basename[0:basename.rfind(".")])(os.path.basename(entry.path))

            layers = compute_image(np.asarray(image), cluster_count, run_count, max_iter_count)
            for i in range(len(layers)):
                layer = layers[i]
                plt.imshow(layer)
                plt.savefig(os.path.join(self.output_folder, f"{input_basename}_layer_{i}.png"))
