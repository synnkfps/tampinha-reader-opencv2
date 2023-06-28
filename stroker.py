import cv2
import numpy as np

INPUT = '2.png' # /outputs/X.png

# settings variables (dicts are mutable globally)
settings = {"X_STEP": 3, "Y_STEP": 3, "RECT_WIDTH": 2, "RECT_HEIGHT": 2, "SHOW_UNSET": False, "FILL_UNSET": False}
# colors variables, BGR cuz opencv2 is :skull:
colors = {"EMPTY_B": 0, "EMPTY_G": 0, "EMPTY_R": 255} 

cv2.namedWindow('image', cv2.WINDOW_KEEPRATIO)
cv2.setWindowProperty('image', 1, cv2.WINDOW_NORMAL)

# main render pipeline
def render():
    RESOLUTION_SCALE = 0.5 # image scaling (later ill add trackbar support)

    image = cv2.imread('outputs/'+INPUT)
    image = cv2.resize(image, (int(image.shape[1]*(RESOLUTION_SCALE)), int(image.shape[0]*(RESOLUTION_SCALE))))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # rectangle calculations
    r_w = settings['X_STEP'] + settings['RECT_WIDTH']
    r_h = settings['Y_STEP'] + settings['RECT_HEIGHT']

    # step Y and step X
    for y in range(0, gray.shape[0], settings['Y_STEP']):
        for x in range(0, gray.shape[1], settings['X_STEP']):
            region = gray[y:y+settings['Y_STEP'], x:x+settings['X_STEP']] # not sure if its a square, i may be checking soon

            # undetected areas
            if settings['SHOW_UNSET']: 
                cv2.rectangle(image, (x, y), (x+r_w, y+r_h), (colors['EMPTY_B'], colors['EMPTY_G'], colors['EMPTY_R']), -1 if settings['FILL_UNSET'] else 1)
            
            # detected areas
            if np.any(region < 255): 
                cv2.rectangle(image, (x, y), (x+r_w, y+r_h), (0, 0, 0), -1)

    cv2.imshow('image', image)

render() # initial rendering
# image trackbars
cv2.createTrackbar('X STEPS', 'image', settings['X_STEP'], 60, lambda value: (settings.update({"X_STEP": value}), render()))
cv2.createTrackbar('Y STEPS', 'image', settings['Y_STEP'], 60, lambda value: (settings.update({"Y_STEP": value}), render()))
cv2.createTrackbar('R. WIDTH', 'image', settings['RECT_WIDTH'], 100, lambda value: (settings.update({"RECT_WIDTH": value}), render()))
cv2.createTrackbar('R. HEIGHT', 'image', settings['RECT_HEIGHT'], 100, lambda value: (settings.update({"RECT_HEIGHT": value}), render()))

# grid trackbars
cv2.namedWindow('grid')
cv2.createTrackbar('Show Empty', 'grid', settings['SHOW_UNSET'], 1, lambda value: (settings.update({"SHOW_UNSET": True if value==1 else False}), render()))
cv2.createTrackbar('Fill Empty', 'grid', settings['FILL_UNSET'], 1, lambda value: (settings.update({"FILL_UNSET": True if value==1 else False}), render()))
cv2.createTrackbar('Empty R', 'grid', colors['EMPTY_R'], 255, lambda value: (colors.update({"EMPTY_R": value}), render()))
cv2.createTrackbar('Empty G', 'grid', colors['EMPTY_G'], 255, lambda value: (colors.update({"EMPTY_G": value}), render()))
cv2.createTrackbar('Empty B', 'grid', colors['EMPTY_B'], 255, lambda value: (colors.update({"EMPTY_B": value}), render()))

# handlers
cv2.waitKey(0)
cv2.destroyAllWindows()
