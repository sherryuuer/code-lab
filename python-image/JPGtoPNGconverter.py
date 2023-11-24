import sys
import os
from PIL import Image


# grab the two argument
# image_folder = int(sys.argv[1])
# output_folder = int(sys.argv[2])
image_folder = 'C:\\Users\\sherr\\Desktop\\code-lab\\python-image\\image_folder'
output_folder = 'C:\\Users\\sherr\\Desktop\\code-lab\\python-image\\output_folder'
# print(image_folder, output_folder)

# check if new/exists, if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# loop through folder
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}\{filename}')
    filename = os.path.splitext(filename)[0]
    # convert
    # save them to the new folder.
    img.save(f'{output_folder}\{filename}.png', 'png')
print("all done!")
