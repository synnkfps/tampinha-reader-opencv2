# Tampinha Reader 🍾
Little project to make coca cola caps (tampinhas) codes easier to read (free coke)

## 🤔 How does it work?
It's pretty simple.
### Converter:
1. opencv2 converts takes an input and then convert it into a thresholded black and white binary image
2. adjusts the threshold/exposure of the binary image
3. writes/saves it on the output folder

### Reader:
1. takes an output (out of the outputs folder)
2. read the whole binary image
3. each X by Y chunk (`x_step` & `y_step` on the `reader.py` file), it checks if one of the pixels on that chunk is black
4. if its black, it paints the whole chunk black using a rectangle (`rectangle_width` & `rectangle_height` in `reader.py` file)

### 😎 How to use?
1. take a photo of your cap code, it must fill the requirements on the `inputs` folder documentation
2. put the photo on the `inputs` folder
3. go to the converter file and it has the following settings:
	1. `INPUT_NAME`: the name of the image file (including extension) inside the `inputs` folder
	2. `OUTPUT_NAME`: the name of the image file to be saved on the `outputs` folder. (do not put any extensions, it will save as .png by default)
	3. `EXPOSURE`: the amount of exposure the binary image will have, low exposure values = more detailed image as a whole | high exposure values = less detailed image, but different color stuff will be saved
	- you can choose if you want to see the image and if you want to write the image on the `WRITE` and `SHOW` variables
