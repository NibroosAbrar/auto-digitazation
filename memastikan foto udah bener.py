from PIL import Image
import rasterio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

input_path = r"D:\ipb capekk\SKRIPSI COY\Data Drone RGB\DARI LAPTOP BANG NOPAL\hasil clip.tif"
output_dir = r"D:\ipb capekk\SKRIPSI COY\Data Drone RGB\DARI LAPTOP BANG NOPAL\patches_png_clean_bbox_flex"
min_patch_size = 1280
thumbnail_width = 3000  # Gambar diperkecil agar tidak membebani memori

with rasterio.open(input_path) as src:
    img = src.read([1, 2, 3])
    img = np.transpose(img, (1, 2, 0))  # CHW -> HWC
    original_height, original_width = img.shape[:2]

    # Resize gambar besar ke ukuran thumbnail
    resize_factor = thumbnail_width / original_width
    thumbnail = Image.fromarray(img).resize(
        (int(original_width * resize_factor), int(original_height * resize_factor))
    )
    thumbnail_np = np.array(thumbnail)

    # Hitung bounding box non-hitam pada citra asli
    non_black_mask = np.any(img != [0, 0, 0], axis=-1)
    rows = np.any(non_black_mask, axis=1)
    cols = np.any(non_black_mask, axis=0)
    min_row, max_row = np.where(rows)[0][[0, -1]]
    min_col, max_col = np.where(cols)[0][[0, -1]]

    fig, ax = plt.subplots(figsize=(12, 12))
    ax.imshow(thumbnail_np)
    ax.set_title("Patch Overlay on Thumbnail")

    y = min_row
    while y <= max_row:
        patch_height = min(min_patch_size, max_row - y + 1)
        x = min_col
        while x <= max_col:
            patch_width = min(min_patch_size, max_col - x + 1)

            # Scale down koordinat patch agar sesuai thumbnail
            x_s = int(x * resize_factor)
            y_s = int(y * resize_factor)
            w_s = int(patch_width * resize_factor)
            h_s = int(patch_height * resize_factor)

            rect = patches.Rectangle((x_s, y_s), w_s, h_s,
                                     linewidth=1, edgecolor='red', facecolor='none')
            ax.add_patch(rect)
            x += min_patch_size
        y += min_patch_size

    plt.axis("off")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "patch_overlay_thumbnail.png"), dpi=300)
    plt.show()
