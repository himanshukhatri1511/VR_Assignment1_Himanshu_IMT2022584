import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = "coin.png"
image = cv2.imread(image_path)

# Check if image is loaded
if image is None:
    print("Error: Image not loaded. Check the file path or ensure the image exists.")
    exit()

print("Image loaded successfully.")

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (15, 15), 7)

# Apply Otsu's thresholding for segmentation
_, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Apply morphological operations to refine segmentation
kernel = np.ones((3, 3), np.uint8)
binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=2)

# Apply edge detection
edges = cv2.Canny(binary, 100, 200)

# Find contours
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create output image
output = image.copy()
coin_count = 0

# Process each detected contour
for contour in contours:
    if cv2.contourArea(contour) > 300:  # Ignore small noise
        coin_count += 1

        # Fit a circle around the detected coin
        (x, y), radius = cv2.minEnclosingCircle(contour)
        center = (int(x), int(y))
        radius = int(radius)

        # Draw the fitted circle
        cv2.circle(output, center, radius, (0, 255, 0), 2)

# Overlay text with the detected coin count
cv2.putText(output, f"Coins: {coin_count}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

# Convert the final output to RGB
rgb_output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

# Save results
cv2.imwrite("Edge_Detection_Output.jpg", edges)
cv2.imwrite("Segmentation_Output.jpg", binary)
cv2.imwrite("Coin_Detection_Output.jpg", output)

# Display the final detection
plt.imshow(rgb_output)
plt.title(f"Detected Coins: {coin_count}")
plt.axis("off")
plt.show()

# Print the total number of coins detected
print(f"Total number of coins detected: {coin_count}")
