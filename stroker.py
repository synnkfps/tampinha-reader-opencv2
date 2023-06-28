import cv2
import numpy as np
import time

print('Processing the image...')
s = time.time()
# Carregar a imagem
image = cv2.imread('outputs/2.png')
RESOLUTION_SCALE = 0.5
image = cv2.resize(image, (int(image.shape[1]*(RESOLUTION_SCALE)), int(image.shape[0]*(RESOLUTION_SCALE))))

# Converter para escala de cinza
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('original', gray)

e = time.time()
print(f'Image Processing took {e-s:.3f}s')

# Definir o tamanho do retângulo
x_step = 3
y_step = 3

rectangle_width = 2
rectangle_height = 2

r_w = x_step+rectangle_width
r_h = y_step+rectangle_height

SHOW_UNSET = False
FILL_UNSET = True

print('Redering the image...')
s = time.time()

# Percorrer a imagem com um passo de 10 pixels ao longo dos eixos x e y
for y in range(0, gray.shape[0], y_step):
    for x in range(0, gray.shape[1], x_step):
        # Extrair a região de pixels
        region = gray[y:y+y_step, x:x+x_step]

        if SHOW_UNSET: cv2.rectangle(image, (x, y), (x+r_w, y+r_h), (230, 230, 230), -1 if FILL_UNSET else 1)
        
        # Verificar se existe pelo menos um pixel preto na região
        if np.any(region < 255):
            cv2.rectangle(image, (x, y), (x+r_w, y+r_h), (0, 0, 0), -1)

else:
    print('Image is being displayed.')
e = time.time()
print(f'Image rendering took {e-s:.2f}s')

# Exibir a imagem modificada
cv2.imshow('Imagem', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
