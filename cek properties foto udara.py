import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling
from rasterio.io import MemoryFile

def reproject_to_utm(src):
    dst_crs = 'EPSG:32749'  # Contoh: UTM Zona 48S, sesuaikan dengan lokasi datanya
    transform, width, height = calculate_default_transform(
        src.crs, dst_crs, src.width, src.height, *src.bounds)
    
    kwargs = src.meta.copy()
    kwargs.update({
        'crs': dst_crs,
        'transform': transform,
        'width': width,
        'height': height
    })
    
    memfile = MemoryFile()
    with memfile.open(**kwargs) as dst:
        for i in range(1, src.count + 1):
            reproject(
                source=rasterio.band(src, i),
                destination=rasterio.band(dst, i),
                src_transform=src.transform,
                src_crs=src.crs,
                dst_transform=transform,
                dst_crs=dst_crs,
                resampling=Resampling.nearest)
        return dst

# Buka raster
with rasterio.open("D:/ipb capekk/SKRIPSI COY/Data Drone RGB/DARI LAPTOP BANG NOPAL/hasil orthomosaic tif mode.tif") as src:
    if src.crs.is_geographic:
        # Reproject ke UTM (meter) jika masih dalam derajat
        with reproject_to_utm(src) as utm_src:
            res_x, res_y = utm_src.res
            pixel_area = abs(res_x * res_y)
            total_pixels = utm_src.width * utm_src.height
            total_area_m2 = total_pixels * pixel_area
    else:
        # Jika sudah dalam meter, langsung hitung
        res_x, res_y = src.res
        pixel_area = abs(res_x * res_y)
        total_pixels = src.width * src.height
        total_area_m2 = total_pixels * pixel_area

    print("Ukuran piksel (meter):", res_x, "x", res_y)
    print("Luas area total (m²):", total_area_m2)
    print("Luas area total (hektar):", total_area_m2 / 10000)
