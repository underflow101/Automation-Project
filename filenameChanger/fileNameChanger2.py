import os

i = 0

for filename in os.listdir("/home/bearpaek/data/datasets/lpl/sleep/"): 
    dst = str(i) + ".jpg"
    src = '/home/bearpaek/data/datasets/lpl/sleep/' + filename 
    dst = '/home/bearpaek/data/datasets/lpl/sleep/' + dst 
    
    os.rename(src, dst) 
    i += 1