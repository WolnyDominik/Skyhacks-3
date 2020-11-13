import tensorflow as tf
from pathlib import Path
import os


train_path = Path('training_images')
live_test_path = Path('live_test_images')

# file_to_open = path_variable/'filename_string'
# f = open(file_to_open)
# print(f.read())

print(tf.__version__)

path = './training_images/'
for filename in os.listdir(path):
    print(path+filename)