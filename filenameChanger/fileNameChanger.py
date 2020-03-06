import os

for i in range(20000):
    os.rename(r'/home/bearpaek/data/datasets/lpl/writing/*.jpg', \
              r'/home/bearpaek/data/datasets/lpl/writing/{}.jpg'.format(i))