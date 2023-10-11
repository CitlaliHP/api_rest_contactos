from PIL import Image
im = Image.open("20221126_095059.jpg")

print(im.format, im.size, im.mode)

"""
box = (0, 0, 400, 400)
region = im.crop(box)

region.save("recorte.png")
"""

r, g, b = im.split()
region = Image.merge("RGB", (b, g, r))
region.save("cambio.png")