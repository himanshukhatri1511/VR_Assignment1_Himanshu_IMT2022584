# Computer Vision Assignment 1  
### Himanshu Khatri - IMT2022584  

## 📌 Overview  
This repository contains solutions for Computer Vision Assignment 1, which consists of two main tasks:  
1. **Coin Detection and Segmentation** – Detecting, segmenting, and counting Indian coins in an image.  
2. **Image Stitching** – Creating a stitched panorama from multiple overlapping images.  

All implementations are in **Python**, and the report is provided in **LaTeX** format.  

---

## 📂 Repository Structure  

```
VR_Assignment1_Himanshu_IMT2022584/
│── unstitchedImages/             # Folder containing images for panorama stitching
│── coin_image.png                # Input image containing scattered Indian coins
│── Edge_Detection_Output.jpg     # Output image after edge detection
│── Segmentation_Output.jpg       # Output image after segmentation
│── Coin_Detection_Output.jpg     # Final output showing detected and counted coins
│── input_image_1.jpeg            # First input image for panorama stitching
│── input_image_2.jpeg            # Second input image for panorama stitching
│── input_image_3.jpeg            # Third input image for panorama stitching
│── keypoints_image_1.png         # ORB keypoints detected in first image
│── keypoints_image_2.png         # ORB keypoints detected in second image
│── keypoints_image_3.png         # ORB keypoints detected in third image
│── stitchedOutput.png            # Initial stitched output
│── stitchedOutputProcessed.png   # Final processed stitched image
│── Q1_CoinDetection.py           # Python script for coin detection and segmentation
│── Q2_ImageStitching.py          # Python script for panorama image stitching
│── README.md                     # Project documentation
│── report.tex                    # LaTeX report source file
│── report.pdf                     # Final report in PDF format
```

---

## 🛠️ Dependencies  
Ensure the following Python packages are installed before running the scripts:  

```bash
pip install opencv-python numpy matplotlib imutils
```

---

## 🔧 Execution Instructions  
Run each script separately from the terminal or command prompt.  

### **1️⃣ Coin Detection and Segmentation**  
```bash
python Q1_CoinDetection.py
```
**Expected Outputs:**  
- `Edge_Detection_Output.jpg` (Edges detected in the coin image)  
- `Segmentation_Output.jpg` (Segmented coins)  
- `Coin_Detection_Output.jpg` (Final output with detected coins and total count)  

### **2️⃣ Image Stitching (Panorama Creation)**  
```bash
python Q2_ImageStitching.py
```
**Expected Outputs:**  
- `keypoints_image_1.png`, `keypoints_image_2.png`, `keypoints_image_3.png` (Keypoints detected in images)  
- `stitchedOutput.png` (Initial stitched image)  
- `stitchedOutputProcessed.png` (Final processed stitched output)  

---

## 📊 Methodology  

### **Part 1: Coin Detection and Segmentation**  
#### 🔹 **Steps Followed:**  
1. Convert the image to grayscale.  
2. Apply Gaussian blur to remove noise.  
3. Use **Otsu’s Thresholding** to segment coins from the background.  
4. Apply **morphological operations** to refine segmentation.  
5. Use **Canny Edge Detection** to detect coin boundaries.  
6. Find **contours** of coins and fit **minimum enclosing circles**.  
7. Count the total coins detected and overlay the count on the final output.  

#### 📌 **Observations:**  
- Edge detection works well but introduces noise.  
- Otsu’s thresholding effectively isolates coins but may over-segment due to similar background intensities.  
- The final detection correctly identifies and counts coins, demonstrating robustness.  

---

### **Part 2: Image Stitching**  
#### 🔹 **Steps Followed:**  
1. Load multiple overlapping images.  
2. Use **ORB Feature Detector** to extract keypoints and descriptors.  
3. Match keypoints across images.  
4. Use OpenCV’s **Stitcher class** to align and merge images into a panorama.  
5. Remove black borders from the final stitched image.  

#### 📌 **Observations:**  
- **Keypoint Detection Efficiency**: ORB effectively detects keypoints but struggles in low-texture regions.  
- **Stitching Accuracy**: Works well when images have sufficient overlap.  
- **Challenges Encountered**:  
  - Poor keypoint matching can lead to misalignment.  
  - Lighting variations cause visible seams.  
- **Potential Improvements**: Using multi-band blending can enhance seamless transitions.  

---

## 📎 Submission Checklist  
✅ **GitHub Repository Name**: `VR_Assignment1_Himanshu_IMT2022584`  
✅ **Two Python Scripts** (`Q1_CoinDetection.py`, `Q2_ImageStitching.py`)  
✅ **README File** (This document)  
✅ **Labeled Visual Outputs** (Edge detection, segmentation, keypoints, stitched image)  
✅ **Captured Images** in `unstitchedImages/` folder  
✅ **Executable Code** (Runs without manual intervention, dependencies are listed)  

---

## 🎯 Conclusion  
This project successfully demonstrates the use of **Computer Vision** techniques for:  
- **Object detection and segmentation** (Coin detection).  
- **Feature matching and image stitching** (Panorama generation).  

The methods used provide accurate results, though further improvements like **multi-band blending** for seamless stitching can be explored.  

---

## 📝 Author  
**Himanshu Khatri**  
IMT2022584  
