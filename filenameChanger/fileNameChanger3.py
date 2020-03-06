import os

i = 0

for filename in os.listdir("/home/bearpaek/data/datasets/lpl/phoneWithHand/"): 
    dst = str(i) + ".jpg"
    src = '/home/bearpaek/data/datasets/lpl/phoneWithHand/' + filename 
    dst = '/home/bearpaek/data/datasets/lpl/phoneWithHand/' + dst 
    
    os.rename(src, dst) 
    i += 1