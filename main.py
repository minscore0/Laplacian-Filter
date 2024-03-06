import numpy as np
import cv2

img_name = input("Name of image: ")
# read input image as grayscale
img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)

height = img.shape[0]
width = img.shape[1]

img_pad = np.pad(img, ((1, 1), (1, 1)), 'edge')

# scalar used in adjusting laplacian filter
w = 1.2

laplacian_filter = np.array([[0, 1, 0],
                            [1, -4, 1],
                             [0, 1, 0]])

laplacian_img = np.zeros((height, width))
laplacian_img = np.pad(laplacian_img, ((1, 1), (1, 1)), 'constant')

for i in range(1, height - 1):
    for j in range(1, width - 1):

        laplacian_img[i, j] = np.sum(img_pad[i-1:i+2, j-1:j+2] * laplacian_filter) * w

# img tyep is uint8 and edge_pad is float64, the result is float64
out_img = img - laplacian_img[1:laplacian_img.shape[0] - 1, 1:laplacian_img.shape[1] - 1]
out_img = np.clip(out_img, 0, 255).astype(np.uint8)  # Clip range to [0, 255] and cast to uint8

#cv2.imwrite(f'{img_name.split(".")[0]}_edge_pad.png', edge_pad-edge_pad.min())/(edge_pad.max() - edge_pad.min())
cv2.imwrite(f'{img_name.split(".")[0]}_laplacian_img.png', out_img)  # Save out_img as PNG image file

# show images
cv2.imshow('img', img)
cv2.imshow('laplacian_img', (laplacian_img-laplacian_img.min())/(laplacian_img.max() - laplacian_img.min()))
cv2.imshow('out_img', out_img)
cv2.waitKey()
cv2.destroyAllWindows()