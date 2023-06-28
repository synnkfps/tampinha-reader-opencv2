import cv2

def zoom_image(img, zoom=1):
    cy, cx = [int(img.shape[0]/2), int(img.shape[1]/2)]
    
    rot_mat = cv2.getRotationMatrix2D((cx,cy), 0, zoom)
    result = cv2.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv2.INTER_LINEAR)
    
    return result

# Variables
INPUT_NAME = '2.jpg' # inputs/input_name
OUTPUT_NAME = f'{INPUT_NAME[:INPUT_NAME.index(".")]}.png' # outputs/X.png

WRITE = True
SHOW = True

SCALE = 0.5

# Settings dict (cuz dict is globally mutable)
settings = {"ZOOM": 3, "EXPOSURE": 9, "BLOCK_SIZE": 21,"USE_ADAPTIVE": True, "ADAPTIVE_METHOD": cv2.ADAPTIVE_THRESH_GAUSSIAN_C}

# Render "Pipeline"
# renders everything in a single trigger
def render():
    # process image
    img = cv2.imread(f'inputs/{INPUT_NAME}')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = zoom_image(img, settings['ZOOM'])
    img = cv2.resize(img, (int(img.shape[1]*SCALE), int(img.shape[0]*SCALE)))

    output_img = img
    # Adaptive Threshold do not need to be an array variable (_,var)
    if settings['USE_ADAPTIVE']: 
        output_img = cv2.adaptiveThreshold(img, 255, settings['ADAPTIVE_METHOD'], cv2.THRESH_BINARY, settings['BLOCK_SIZE'], settings['EXPOSURE'])
    else: 
        # binary/normal threshold do not use BLOCK_SIZE
        rect,output_img = cv2.threshold(img, settings['EXPOSURE'], 255, cv2.THRESH_BINARY)
    
    cv2.imshow('Thresholded Image', output_img) # self explanatory
    if WRITE: 
        cv2.imwrite(f'outputs/{OUTPUT_NAME}', output_img)

# Window Properties
cv2.namedWindow('Thresholded Image', cv2.WINDOW_KEEPRATIO)
cv2.resizeWindow('Thresholded Image', 600, 900)
cv2.setWindowProperty('image', 1, cv2.WINDOW_NORMAL)

# Trackbars with lambda trick
cv2.createTrackbar('Exposure', 'Thresholded Image', settings['EXPOSURE'], 255, lambda value: (settings.update({'EXPOSURE': value}), render()))
cv2.createTrackbar('Block Size', 'Thresholded Image', settings['BLOCK_SIZE'], 60, lambda value: (settings.update({'BLOCK_SIZE': value if value>1 and value%2!=0 else settings['BLOCK_SIZE']}), render()))
cv2.createTrackbar('Adaptive', 'Thresholded Image', settings['USE_ADAPTIVE'], 1, lambda value: (settings.update({'USE_ADAPTIVE': value == 1}), render()))
cv2.createTrackbar('Adap. Method', 'Thresholded Image', settings['ADAPTIVE_METHOD'], 1, lambda value: (settings.update({'ADAPTIVE_METHOD': cv2.ADAPTIVE_THRESH_GAUSSIAN_C if value == 0 else cv2.ADAPTIVE_THRESH_MEAN_C}), render()))
cv2.createTrackbar('Zoom', 'Thresholded Image', 1, 10, lambda value: (settings.update({'ZOOM': value}), render()))

# Window Closing Callbacks
cv2.waitKey(0)
cv2.destroyAllWindows()
