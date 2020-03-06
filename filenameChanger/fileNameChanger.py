import os

i = 0

for filename in os.listdir("/home/bearpaek/data/datasets/lpl/writing/"): 
    dst = str(i) + ".jpg"
    src = '/home/bearpaek/data/datasets/lpl/writing/' + filename 
    dst = '/home/bearpaek/data/datasets/lpl/writing/' + dst 
    
    os.rename(src, dst) 
    i += 1