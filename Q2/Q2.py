import numpy as np
import cv2
import glob
import imutils
import matplotlib.pyplot as plt

# Get the list of all image paths inside the 'unstitchedImages' folder
image_paths = glob.glob('unstitchedImages/*.jpeg')
images = []  # List to store the loaded images

# Load each image, display it, and store it in the list
for image in image_paths:
    img = cv2.imread(image)
    images.append(img)  # Add the image to the list
    cv2.imshow("Image", img)  # Show the image to check if it's loaded correctly
    cv2.waitKey(0)  # Wait for a key press before moving to the next image

# Initialize ORB (Oriented FAST and Rotated BRIEF) feature detector
orb = cv2.ORB_create()

# Detect keypoints in each image and visualize them
for i, img in enumerate(images):
    keypoints = orb.detect(img, None)  # Detect keypoints
    keypointsImage = cv2.drawKeypoints(img, keypoints, None, color=(0, 255, 0))  # Draw keypoints

    # Convert the image to RGB for correct display in Matplotlib
    img_rgb = cv2.cvtColor(keypointsImage, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(10, 6))
    plt.imshow(img_rgb)
    plt.title(f"Keypoints in Image {i+1}")  # Give each image a title
    plt.axis("off")  # Hide axis labels for better visualization
    plt.show()

# Create a Stitcher instance to stitch images together
imageStitcher = cv2.Stitcher_create()
error, stitched_img = imageStitcher.stitch(images)  # Try stitching the images

if not error:
    # Save and display the stitched output image
    cv2.imwrite("stitchedOutput.png", stitched_img)
    cv2.imshow("Stitched Img", cv2.resize(stitched_img, (600, 600)))  # Resize for better visibility
    cv2.waitKey(0)

    # Add a black border around the stitched image to ensure cleaner processing
    stitched_img = cv2.copyMakeBorder(stitched_img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, (0, 0, 0))

    # Convert to grayscale and apply thresholding to create a binary image
    gray = cv2.cvtColor(stitched_img, cv2.COLOR_BGR2GRAY)
    thresh_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]

    # Display the thresholded image
    cv2.imshow("Threshold Image", cv2.resize(thresh_img, (600, 600)))
    cv2.waitKey(0)

    # Find contours in the binary image to identify the stitched region
    contours = cv2.findContours(thresh_img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    areaOI = max(contours, key=cv2.contourArea)  # Get the largest contour, assuming it's the main stitched area

    # Create a mask of the detected stitched area
    mask = np.zeros(thresh_img.shape, dtype="uint8")
    x, y, w, h = cv2.boundingRect(areaOI)  # Get bounding box coordinates
    cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)  # Draw rectangle on the mask

    # Initialize a copy of the mask for further refinement
    minRectangle = mask.copy()
    sub = mask.copy()

    # Perform erosion until the noise is removed and only the stitched region remains
    while cv2.countNonZero(sub) > 0:
        minRectangle = cv2.erode(minRectangle, None)
        sub = cv2.subtract(minRectangle, thresh_img)

    # Find contours again after refining the mask
    contours = cv2.findContours(minRectangle.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    areaOI = max(contours, key=cv2.contourArea)  # Get the main region of interest again

    # Display the refined stitched region mask
    cv2.imshow("minRectangle Image", minRectangle)
    cv2.waitKey(0)

    # Crop the stitched image to remove extra black borders
    x, y, w, h = cv2.boundingRect(areaOI)
    stitched_img = stitched_img[y:y + h, x:x + w]  # Crop the image using bounding box coordinates

    # Save and display the final cleaned-up stitched image
    cv2.imwrite("stitchedOutputProcessed.png", stitched_img)
    cv2.imshow("Stitched Image Processed", cv2.resize(stitched_img, (600, 600)))
    cv2.waitKey(0)

else:
    # If stitching fails, print an error message
    print("Images could not be stitched!")
    print("Likely not enough keypoints being detected!")
