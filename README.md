# Tampinha Reader 🍾
Little project to make coca cola caps (tampinhas) codes easier to read (free coke)

### 😎 How to use?
1. take a photo of your cap code, it must fill the requirements on the `inputs` folder documentation
2. put the photo on the `inputs` folder
3. go to the `main` file, and edit the `image` variable with the name of your image (`cv2.imread("name of the image.jpg")`)
4. run the file

And there you will have some sliders, which you can adjust for better reading.
### 🛹 Sliders
- Threshold: Exposure of the pixels
	- High Values: clearer, can perceive small details (optimal)
	- Low Values: noisy, highly detailed
- Block Size: "Weight" of each detected exposed pixel
	- High Values: bolder details
	- Low Values: sharper lighter details
- Use Adaptive: Uses a different algorithm of exposure
	- On (1): better than binary (non adaptive), adapts light
	- Off (0): worse than adaptive, literally trash
- Use OTSU: Uses some guy's method, only works with non inversed binary (not adaptive)
	- On (1): :skull:
	- Off (0): better than on
- Inverted: inverts the image colors (bw -> wb)
