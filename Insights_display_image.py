import random
import os

dir_folder = "/home/karthik/Desktop/CSE/InsightsonIndia/"

rnd_dir = dir_folder + random.choice(os.listdir(dir_folder))
a = rnd_dir + '/' +random.choice(os.listdir(rnd_dir))
b = "eog -f " + a

os.system(b)




