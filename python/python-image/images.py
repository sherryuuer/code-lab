from PIL import Image
# from PIL import ImageFilter


im_pika = Image.open(
    r"C:\Users\sherr\Desktop\code-lab\python-image\pikachu.jpg")
im_pic = Image.open(r"C:\Users\sherr\Desktop\code-lab\python-image\pic.jpg")
# print(im.format, im.size, im.mode)

# 显示图片
# im.show()
# print(im.mode)

# out_pic = im_pic.resize((500, 650))
# 确保长宽比
im_pic.thumbnail((400, 400))
print(im_pic.format, im_pic.size, im_pic.mode)
im_pic.save(r"C:\Users\sherr\Desktop\code-lab\python-image\pic_thumbnail.jpg")
# out = out.rotate(45)  # degrees counter-clockwise
# out = out.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
# out = out.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
# out = out.transpose(Image.Transpose.ROTATE_90)
# filtered = im_pic.filter(ImageFilter.BLUR)
# out = out.convert("L")
box = (100, 100, 400, 400)
out = im_pika.crop(box=box)
out.save(r"C:\Users\sherr\Desktop\code-lab\python-image\pikachu_face.jpg")
