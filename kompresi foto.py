from PIL import Image
import rasterio
from rasterio.enums import Resampling
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog

def compress_and_remove_black_background(input_tif_path, output_png_path, 
                                         scale_factor=0.08, bg_threshold=15):
    with rasterio.open(input_tif_path) as src:
        width = int(src.width * scale_factor)
        height = int(src.height * scale_factor)
        data = src.read(
            indexes=[1, 2, 3],
            out_shape=(3, height, width),
            resampling=Resampling.bilinear)
        transform = src.transform * src.transform.scale(
            (src.width / width),
            (src.height / height))

    if data.dtype != np.uint8:
        data = ((data - data.min()) / (data.max() - data.min()) * 255).astype(np.uint8)
    
    r, g, b = data
    mask = ~((r < bg_threshold) & (g < bg_threshold) & (b < bg_threshold))  
    alpha = (mask * 255).astype(np.uint8)
    rgba = np.stack([r, g, b, alpha], axis=-1)  # (H, W, 4)
    img = Image.fromarray(rgba, mode='RGBA')
    img.save(output_png_path, format='PNG', optimize=True)

    # Simpan worldfile (.pngw)
    a = transform.a
    e = transform.e
    x0 = transform.c
    y0 = transform.f
    worldfile_path = output_png_path + "w"  # PNG worldfile
    with open(worldfile_path, "w") as f:
        f.write(f"{a}\n0.0\n0.0\n{e}\n{x0}\n{y0}\n")

    xmin = x0
    xmax = x0 + (width * a)
    ymax = y0
    ymin = y0 + (height * e)
    bounds = [[ymin, xmin], [ymax, xmax]]

    print(f"✔️ Disimpan ke: {output_png_path}")
    print(f"📐 World file: {worldfile_path}")
    print(f"📦 Ukuran: {os.path.getsize(output_png_path) / (1024 * 1024):.2f} MB")
    print(f"🌍 Bounds: {bounds}")

# ======================= GUI Input/Output ========================

def main():
    root = tk.Tk()
    root.withdraw()

    print("📂 Pilih file .tif input...")
    input_path = filedialog.askopenfilename(title="Pilih file TIF", filetypes=[("GeoTIFF", "*.tif *.tiff")])
    if not input_path:
        print("❌ Tidak ada file dipilih.")
        return

    print("💾 Tentukan lokasi penyimpanan output PNG...")
    output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
    if not output_path:
        print("❌ Lokasi output tidak dipilih.")
        return

    compress_and_remove_black_background(input_path, output_path)

if __name__ == "__main__":
    main()
