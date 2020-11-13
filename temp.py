from model_manager import *
import cv2
import numpy as np

manager = Manager()
manager.loadCsv()

#manager.processAllImagesToBinary(manager.all_image_names.to_numpy())


manager.importTrainingDataFromBinaryFile()
manager.initializeModel()
print(manager.x_test)
print(manager.x_train)
print(manager.y_test)
print(manager.y_train)
