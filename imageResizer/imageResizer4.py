# resize image automation

import glob, os
from PIL import Image

src = "/home/bearpaek/data/datasets/lpl/sleep/"
dst = "/home/bearpaek/data/datasets/lpl224/sleep/"

im_path = glob.glob(os.path.join(src, '*.jpg'))

i = 0

for filename in im_path:
    print(filename)
    img = Image.open(filename)
    im = img.resize((224, 224), Image.ANTIALIAS)
    im.save(dst + str(i) + '.jpg')
    i += 1