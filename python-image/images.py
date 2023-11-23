from PIL import Image, ImageFilter


im = Image.open(r"C:\Users\sherr\Desktop\code-lab\python-image\pikachu.jpg")
# print(im.format, im.size, im.mode)
# im.show()
# print(im.mode)
# out = im.resize((500, 650))
# out = out.rotate(45)  # degrees counter-clockwise
# out = out.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
# out = out.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
# out = out.transpose(Image.Transpose.ROTATE_90)
# out = out.transpose(Image.Transpose.ROTATE_180)
# out = out.transpose(Image.Transpose.ROTATE_270)
filtered = im.filter(ImageFilter.BLUR)
# out = out.convert("L")
box = (100, 100, 400, 400)
out = im.crop(box=box)
out.save(r"C:\Users\sherr\Desktop\code-lab\python-image\pikachu_face.jpg")
