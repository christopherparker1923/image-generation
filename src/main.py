import cv2
from PIL import Image
import matplotlib.pyplot as pyplot
import numpy as np

pyplot.rcParams["figure.figsize"] = (10, 10)

# Open the image file
image = Image.open("./assets/bird.jpg")
# image.show()

image_array = np.array(image)

# pyplot.imshow(image_array)
pyplot.axis("off")


#print("hello")


# detected_edges = cv2.Canny(image_array, 100, 100)

# inverted_image = 255 - detected_edges

# pyplot.imshow(inverted_image, cmap="gray")


# cv2.imwrite("./assets/bird_edges.png", cv2.cvtColor(inverted_image, cv2.COLOR_RGB2BGR))


gray_image = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)

# pyplot.imshow(gray_image, cmap="gray")

cv2.imwrite("./assets/bird_grey.png", gray_image)

pyplot.contour(gray_image, origin="image")

pyplot.show()
