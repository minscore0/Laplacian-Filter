import cv2
import numpy as np

# Read the input image
image = cv2.imread('dog.jpeg', cv2.IMREAD_GRAYSCALE)

# Apply the Laplacian operator
laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Convert the output to an 8-bit unsigned integer
laplacian_uint8 = cv2.convertScaleAbs(laplacian)

# Display the result
cv2.imshow('Laplacian', laplacian_uint8)
cv2.waitKey(0)
cv2.destroyAllWindows()