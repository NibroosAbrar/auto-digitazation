import rasterio
from rasterio.windows import Window
import os
import numpy as np
from PIL import Image

# Path input dan output
input_path = r"D:\ipb capekk\SKRIPSI COY\Data Drone RGB\DARI LAPTOP BANG NOPAL\hasil clip.tif"
output_dir = os.path.join(os.path.dirname(input_path), "patches_png_clean_bbox_flex")
os.makedirs(output_dir, exist_ok=True)

min_patch_size = 1280

with rasterio.open(input_path) as src:
    # Ambil hanya channel RGB
    img = src.read([1, 2, 3])
    img = np.transpose(img, (1, 2, 0))  # CHW -> HWC

    # Cari bounding box non-hitam
    non_black_mask = np.any(img != [0, 0, 0], axis=-1)
    rows = np.any(non_black_mask, axis=1)
    cols = np.any(non_black_mask, axis=0)
    min_row, max_row = np.where(rows)[0][[0, -1]]
    min_col, max_col = np.where(cols)[0][[0, -1]]

    height = max_row - min_row + 1
    width = max_col - min_col + 1

    count = 0
    y = min_row
    while y <= max_row:
        patch_height = min(min_patch_size, max_row - y + 1)
        if y + patch_height > max_row:
            patch_height = max_row - y + 1
        x = min_col
        while x <= max_col:
            patch_width = min(min_patch_size, max_col - x + 1)
            if x + patch_width > max_col:
                patch_width = max_col - x + 1

            window = Window(x, y, patch_width, patch_height)
            patch = src.read([1, 2, 3], window=window)
            patch = np.transpose(patch, (1, 2, 0))

            # Hitung rasio hitam
            black_ratio = np.sum(np.all(patch == [0, 0, 0], axis=-1)) / (patch.shape[0] * patch.shape[1])
            if black_ratio > 0.001:
                x += min_patch_size
                continue

            # Simpan patch
            img_out = Image.fromarray(patch)
            img_out.save(os.path.join(output_dir, f"patch_{count:04d}.png"))
            count += 1

            x += min_patch_size
        y += min_patch_size

print(f"Total patch fleksibel yang disimpan: {count}")
