from PIL import Image
im = Image.open("20221126_095059.jpg")

print(im.format, im.size, im.mode)