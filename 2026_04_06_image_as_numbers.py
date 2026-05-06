import cv2

# load image
img = cv2.imread("sample.jpg")

print("Image Shape:", img.shape)   # (height, width, channels)
print("Pixel Value at (0,0):", img[0,0])
print("Number of Channels:", img.shape[2])