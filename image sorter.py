from pathlib import Path
from shutil import copyfile
import os
import pandas as pd
training_path = Path(__file__).parent.absolute()/'training_images/'
valid_path = Path(__file__).parent.absolute()/'training_images/'

labels = pd.read_csv('training_labels.csv')
columns = labels.columns[1:]
 #print(len(columns))
for path in columns:
     #print(training_path/'xd'/path)
    os.makedirs(training_path/path, exist_ok=True)

print(columns)
for _, row in labels.iterrows():
    for col in columns:
        if row[col]:
            copyfile(training_path/row["Name"], training_path/col/row["Name"])