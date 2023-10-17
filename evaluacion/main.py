from PIL import Image

# Cargar la imagen
imagen = Image.open("imagen1.jpg")

# Verificar el formato, tamaño y modo de la imagen
print(imagen.format, imagen.size, imagen.mode)

# Recortar la imagen
box = (0, 0, 400, 400)
imagen_recortada = imagen.crop(box)
imagen_recortada.save("recorte.png")

# Voltear horizontalmente la imagen
imagen_volteada = imagen.transpose(Image.FLIP_LEFT_RIGHT)
imagen_volteada.save("volteo.png")

# Cambiar los canales de color (R, G, B)
r, g, b = imagen.split()
imagen_colorizada = Image.merge("RGB", (g, b, r))
imagen_colorizada.save("colorize.png")

print("Procesamiento de imagen completado.")
