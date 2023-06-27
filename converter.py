import cv2 

def zoom_image(image, zoom_factor):
    height, width = image.shape[:2]
    new_height = int(height / zoom_factor)
    new_width = int(width / zoom_factor)
    
    # Define the ROI coordinates
    start_row = int((height - new_height) / 2)
    start_col = int((width - new_width) / 2)
    end_row = start_row + new_height
    end_col = start_col + new_width
    
    # Extract the ROI (zoomed portion) from the image
    zoomed_image = image[start_row:end_row, start_col:end_col]

    zoomed_image = cv2.resize(zoomed_image, (width, height))
    
    return zoomed_image

INPUT_NAME = 'tampinha3.jpg'
OUTPUT_NAME = '3'
WRITE = True
SHOW = False

img = cv2.imread(f'inputs/{INPUT_NAME}')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = zoom_image(img, 3)
#cv2.imshow('original', cv2.resize(img, (500, 500)))
img = cv2.resize(img, (500, 500))

EXPOSURE = 9

_, result = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY)

adaptive_result = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 41, EXPOSURE)
if SHOW: 
    cv2.imshow('adapted', adaptive_result)
if WRITE: 
    cv2.imwrite(f'outputs/{OUTPUT_NAME}.png', adaptive_result)

#cv2.imshow('result', result)
#cv2.imshow('original', img)
cv2.waitKey(0)
