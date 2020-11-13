#import tensorflow as tf
from pathlib import Path
import os
import numpy as np
import cv2
import pandas as pd


#train_path = Path('training_images')
#live_test_path = Path('live_test_images')

# file_to_open = path_variable/'filename_string'
# f = open(file_to_open)
# print(f.read())

#print(tf.__version__)

path = './live_test_images/'

files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]

columns = ['Name','Amusement park', 'Animals', 'Bench', 'Building', 'Castle',
       'Cave', 'Church', 'City', 'Cross', 'Cultural institution', 'Food',
       'Footpath', 'Forest', 'Furniture', 'Grass', 'Graveyard', 'Lake',
       'Landscape', 'Mine', 'Monument', 'Motor vehicle', 'Mountains', 'Museum',
       'Open-air museum', 'Park', 'Person', 'Plants', 'Reservoir', 'River',
       'Road', 'Rocks', 'Snow', 'Sport', 'Sports facility', 'Stairs', 'Trees',
       'Watercraft', 'Windows']

df = pd.DataFrame(data=None, index=None, columns=columns, dtype=None, copy=False)

skip = int(input('Skip count: '))
toSkip = skip

i=0
for filename in files:
    toSkip=toSkip-1
    if toSkip > -1:
        continue


    maxwidth, maxheight = 600, 800
    img = cv2.imread(path+filename,3)
    f = min(maxwidth / img.shape[1], maxheight / img.shape[0])
    dim = (int(img.shape[1] * f), int(img.shape[0] * f))
    resized = cv2.resize(img, dim)
    cv2.imshow('out.png', resized)

    outputs = []
    outputs.append(filename)

    for column in columns:
        if column == 'Name':
            continue
        print(column)
        k = cv2.waitKey(0)
        if k  == 32:
            outputs.append(False)
            print(False)
        else:
            outputs.append(True)
            print(True)
        print('')

    df.loc[i] = outputs
    i=i+1
    
    print(i)
    print('Continue?')
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break

df.to_csv(str(skip)+'manual_live_test_output.csv', index=False)