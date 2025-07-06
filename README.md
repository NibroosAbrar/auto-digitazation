# Automatic Object Digitization Using YOLO Segmentation

## Description
This project offers an automated solution for object digitization from large-scale aerial imagery using the YOLO Segmentation algorithm. Designed to overcome the inefficiencies and errors of manual labeling methods, especially in geospatial and agricultural applications, this project enables faster and more accurate data acquisition for critical decision-making.

## Key Features
* **Automated & Efficient Digitization:** Full automation of the object digitization process.
* **Precise Vector Data Output:** Generates vector data with accurate and detailed polygons.
* **High Scalability:** Capable of processing vast areas (dozens to hundreds of hectares) with thousands of objects in hours or even minutes.
* **Supports Accurate Spatial Analysis:** The generated data is vital for in-depth spatial analysis (e.g., crop health monitoring, nutrient assessment).
* **User-Friendly Implementation:** The provided code is designed to be easy to use and customizable.

## Motivation & Problem Solved
Object digitization in imagery is a crucial step for in-depth geospatial and agricultural analysis. However, the manual process is incredibly time-consuming, tedious, and prone to errors, especially for very large areas. This traditional approach often becomes a bottleneck in fulfilling the need for rapid decision-making in time-sensitive operations. This project aims to revolutionize this bottleneck by providing a highly efficient and accurate automated alternative.

## How It Works (High-Level)
This project leverages the power of Deep Learning, specifically the YOLO Segmentation algorithm, to automatically detect and perform object segmentation within aerial imagery. The model is tailored to recognize specific features (e.g., durian tree canopies) and outputs precise vector polygon data, significantly accelerating data acquisition workflows.

## Case Study & Example Application
One successfully demonstrated application is the automated digitization of durian tree canopies from drone imagery. This solution efficiently processed over 2000 objects across a 30-hectare area in approximately 45 minutes to 1 hour, a task that would typically take days if done manually.

## Installation
To set up and run this project, please follow these steps:

**Prerequisites:**
* Python 3.10+
* pip (Python package installer)
* git

**Steps:**
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/NibroosAbrar/auto-digitization.git](https://github.com/NibroosAbrar/auto-digitization.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd auto-digitization
    ```
3.  **Create and activate a virtual environment (highly recommended):**
    * Linux/macOS:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * Windows (PowerShell):
        ```bash
        py -m venv venv
        .\venv\Scripts\activate
        ```
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(**Important:** You need to create a `requirements.txt` file in the root directory of your repository containing a list of all required Python libraries, such as `ultralytics`, `opencv-python`, `numpy`, `rasterio`, `geopandas`, `torch`, `torchvision`, etc.)*

## Usage
Once installed, you can use the provided scripts to process your aerial imagery.

**Input Data:**
* Aerial imagery (e.g., drone photos, satellite images) in common formats (.tif, .jpg, .png).
* Ensure your images are georeferenced for accurate spatial output.

**Available Scripts:**

* ### `kompresi_foto.py` (Image Compression/Preprocessing)
    Use this script to compress or preprocess your input images before running the main inference.
    ```bash
    python kompresi_foto.py --input_dir path/to/your/raw_images --output_dir path/to/save/compressed_images
    ```

* ### `cek_properties_foto_udara.py` (Aerial Image Property Check)
    This script can be used to check the metadata or properties of your aerial imagery.
    ```bash
    python cek_properties_foto_udara.py --image_path path/to/your/image.tif
    ```

* ### `Inferensi model final.py` (Main Inference Script)
    This is the core script for running automated object digitization using the trained YOLO model.
    ```bash
    python "Inferensi model final.py" --image_path path/to/your/processed_image.tif --output_path path/to/save/output_vectors.shp --model_path path/to/your/best_yolo_model.pt
    ```
    *(**Note:** You will need to provide the path to your trained YOLO model file, e.g., `best.pt`)*

**Output:**
* Shapefile (.shp) or other vector formats containing the digitized polygons of detected objects.

## Contact / Author
**Muhammad Nibroos Abrar**
* [LinkedIn Profile](https://www.linkedin.com/in/mnibroosabrar)
* [GitHub Profile](https://github.com/NibroosAbrar)
* [Medium Article](https://medium.com/@mnibroosabrar/no-more-manual-labeling-deep-learning-transforms-spatial-digitization-in-agriculture-c9d89bf98e4f)
