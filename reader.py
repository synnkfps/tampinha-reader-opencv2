import cv2
import numpy as np

# Carregar a imagem
image = cv2.imread('outputs/1.png')
image = cv2.resize(image, (image.shape[1], image.shape[0]))

# Converter para escala de cinza
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Definir o tamanho do retângulo
x_step = 2
y_step = 2

rectangle_width = 1
rectangle_height = 1

r_w = x_step+rectangle_width
r_h = y_step+rectangle_height

# Percorrer a imagem com um passo de 10 pixels ao longo dos eixos x e y
for y in range(0, gray.shape[0], y_step):
    for x in range(0, gray.shape[1], x_step):
        # Extrair a região de pixels
        region = gray[y:y+y_step, x:x+x_step]
        
        # Verificar se existe pelo menos um pixel preto na região
        if np.any(region == 0):
            cv2.rectangle(image, (x, y), (x+r_w, y+r_h), (0, 0, 0), -1)

# Exibir a imagem modificada
cv2.imshow('Imagem', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
