import cv2

image = cv2.imread("inputs/tampinha3.jpg") # your input image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

vars = {"EXPOSURE": 6, "USE_ADAPTIVE": 0, "BLOCK_SIZE": 41, "USE_OTSU": 1, "INVERTED": 0}

def render():
    if vars['USE_ADAPTIVE'] == 0:
        t_type = cv2.THRESH_OTSU if vars['USE_OTSU'] == 1 else cv2.THRESH_BINARY if vars['INVERTED'] == 0 else cv2.THRESH_BINARY_INV
        _, thresholded = cv2.threshold(gray_image, vars['EXPOSURE'], 255, t_type)
    
    if vars['USE_ADAPTIVE'] == 1:
        thresholded = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY if vars['INVERTED'] == 0 else cv2.THRESH_BINARY_INV, vars['BLOCK_SIZE'], vars['EXPOSURE'])
    
    cv2.namedWindow('Thresholded Image',  cv2.WINDOW_NORMAL)
    cv2.imshow("Thresholded Image", thresholded)
    cv2.setWindowProperty('Thresholded Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

cv2.namedWindow('Parameters')
# Hacky lambda way so i dont need to add functions
cv2.createTrackbar('Threshold', 'Parameters', vars['EXPOSURE'], 150, lambda x: (vars.update({"EXPOSURE": x}), render()))
cv2.createTrackbar('Block Size', 'Parameters', vars['BLOCK_SIZE'], 100, lambda x: (vars.update({"BLOCK_SIZE": x if x>1 and x%2!=0 else vars['BLOCK_SIZE']}), render()))
cv2.createTrackbar('Use Adaptive', 'Parameters', vars['USE_ADAPTIVE'], 1, lambda x: (vars.update({"USE_ADAPTIVE": x}), render()))
cv2.createTrackbar('Use OTSU', 'Parameters', vars['USE_OTSU'], 1, lambda x: (vars.update({"USE_OTSU": x}), render()))
cv2.createTrackbar('Inverted', 'Parameters', vars['INVERTED'], 1, lambda x: (vars.update({"INVERTED": x}), render()))

while True:
    render()
    
    if cv2.waitKey(1) == 27 or cv2.waitKey(0):
        break

cv2.destroyAllWindows()
