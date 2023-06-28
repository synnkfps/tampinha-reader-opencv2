# Tampinha Reader 🍾
Little project to make coca cola caps (tampinhas) codes easier to read (free coke)

### 😎 How to use?
1. take a photo of your cap code, it must fill the requirements on the `inputs` folder documentation
2. put the photo on the `inputs` folder
3. go to the `main` file, and edit the `image` variable with the name of your image (`cv2.imread("name of the image.jpg")`)
4. run the file

# Program Documentation

This program consists of two files: `main.py` and `stroker.py`. Each file has its own functionality and set of variables. Below, you'll find an overview of how both files work, their variables, and what each setting does.

## `main.py`

This file contains the main pipeline for image processing and thresholding. It utilizes the OpenCV library to perform various operations on the input image.

### Variables

- `INPUT_NAME`: Name of the input image file (e.g., `'2.jpg'`)
- `OUTPUT_NAME`: Name of the output image file (e.g., `'2.png'`)
- `WRITE`: Boolean flag to enable/disable writing the output image to a file
- `SHOW`: Boolean flag to enable/disable displaying the thresholded image
- `SCALE`: Scaling factor for resizing the image
- `settings`: Dictionary containing various settings for image processing, such as zoom level, exposure, block size, adaptive thresholding, and adaptive method

### `zoom_image` Function

- `zoom_image(img, zoom=1)`: Zooms the input image by a specified factor. It uses the `cv2.getRotationMatrix2D` and `cv2.warpAffine` functions to achieve the zoom effect.

### `render` Function

This function represents the rendering pipeline, which processes the input image and displays the thresholded image.

### Window Properties

- The window named `'Thresholded Image'` is created with the `cv2.namedWindow` function.
- The window size is set using `cv2.resizeWindow`.
- The window property is set to `cv2.WINDOW_NORMAL` to allow resizing.

### Trackbars and Callbacks

- Trackbars are created using the `cv2.createTrackbar` function.
- The lambda trick is used to update the corresponding settings dictionary and trigger the `render` function.
- Trackbars are provided for adjusting the exposure, block size, adaptive thresholding, adaptive method, and zoom level.

### Window Closing

- The `cv2.waitKey` function waits for a key press.
- The `cv2.destroyAllWindows` function is used to close all created windows.

## `stroker.py`

This file contains the main pipeline for stroke detection and visualization. It utilizes the OpenCV library for image processing.

### Variables

- `INPUT`: Name of the input image file (e.g., `'2.png'`)
- `settings`: Dictionary containing various settings for stroke detection, such as step size, rectangle width and height, and options for displaying and filling unset areas.
- `colors`: Dictionary containing color values (BGR) for empty areas.

### `render` Function

This function represents the rendering pipeline for stroke detection. It loads the input image, performs necessary preprocessing, and detects strokes using rectangle calculations.

### Window Properties

- The window named `'image'` is created with the `cv2.namedWindow` function.
- The window property is set to `cv2.WINDOW_NORMAL` to allow resizing.

### Trackbars and Callbacks

- Trackbars are created using the `cv2.createTrackbar` function.
- The lambda trick is used to update the corresponding settings dictionary and trigger the `render` function.
- Trackbars are provided for adjusting the step size, rectangle width and height.

### Grid Trackbars

- Another window named `'grid'` is created to control grid-related settings.
- Trackbars are provided for showing/filling empty areas, and adjusting color values for empty areas.

### Window Closing

- The `cv2.waitKey` function waits for a key press.
- The `cv2.destroyAllWindows` function is used to close all created windows.


