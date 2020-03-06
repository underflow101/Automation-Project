import os

i = 0

for filename in os.listdir("/home/bearpaek/data/datasets/lpl/others/"): 
    dst = str(i) + ".jpg"
    src = '/home/bearpaek/data/datasets/lpl/others/' + filename 
    dst = '/home/bearpaek/data/datasets/lpl/others/' + dst 
    
    os.rename(src, dst) 
    i += 1