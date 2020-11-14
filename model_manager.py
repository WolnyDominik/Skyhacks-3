import tensorflow as tf
keras = tf.keras
layers = keras.layers

import pandas as pd
import os
import math
import cv2
import numpy as np

#from keras.applications.resnet50 import preprocess_input
#from keras.preprocessing.image import ImageDataGenerator

training_data_folder = r"."
csv_path = os.path.join(training_data_folder, "training_labels.csv")
csv_test_path = os.path.join(training_data_folder, "training_labels_test.csv")
csv_train_path = os.path.join(training_data_folder, "training_labels_train.csv")
photos_path = os.path.join(training_data_folder, "training_images")
bin_photos_path = os.path.join(training_data_folder, "training_images.bin")
models_path = os.path.join(training_data_folder, "models")
live_test_path = os.path.join(training_data_folder, "live_test_images")

RESOLUTION = 224


columns = ['Name', 'Amusement park', 'Animals', 'Bench', 'Building', 'Castle',
       'Cave', 'Church', 'City', 'Cross', 'Cultural institution', 'Food',
       'Footpath', 'Forest', 'Furniture', 'Grass', 'Graveyard', 'Lake',
       'Landscape', 'Mine', 'Monument', 'Motor vehicle', 'Mountains', 'Museum',
       'Open-air museum', 'Park', 'Person', 'Plants', 'Reservoir', 'River',
       'Road', 'Rocks', 'Snow', 'Sport', 'Sports facility', 'Stairs', 'Trees',
       'Watercraft', 'Windows']

def seperateTests(test_rate = 0.1, path = csv_path, test_path = csv_test_path, train_path = csv_train_path):
    print("Seperating tests...")
    csv_data = pd.read_csv(path)
    tests_n = math.ceil(csv_data.shape[0] * test_rate)
    
    csv_test_data = csv_data[0:tests_n]
    csv_train_data = csv_data[tests_n:]
    
    csv_test_data.to_csv(test_path, index=False)
    csv_train_data.to_csv(train_path, index=False)
    print("Done")

  
    
def proccessAllImages( paths):
    size = len(paths)
    images = np.empty([size, RESOLUTION, RESOLUTION, 3])
    for i in range(0, size):
        print("  ", i, " / ", size)
        images[i] = processImage(paths[i])
    return images

def processImage(path):
    image = cv2.imread(path)
    return cv2.cvtColor(cv2.resize(image, (RESOLUTION, RESOLUTION)), cv2.COLOR_BGR2RGB)

def processAllImagesToBinary(names_list = None, bin_path = bin_photos_path, images_path = photos_path, start_i = 0, count = -1):
    print("Processing images...")
    if(names_list == None):
        names_list = np.array([file for file in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, file))])
    end_i = names_list.size
    if count > 0:
        end_i = math.min(start_i + count, end_i)
    imagesData = np.empty([end_i-start_i,RESOLUTION,RESOLUTION,3], dtype=np.uint8)
    for i in range(start_i, end_i):
        print("  ", i-start_i, " / ", end_i-start_i)
        imagesData[i] = processImage( os.path.join(images_path, names_list[i]) )
    print("SavingToBinary...")
    imagesData.tofile(bin_path)
    print("Done")

def importImagesFromBinaryFile(path_to_file):
    return np.fromfile(path_to_file, dtype=np.uint8).reshape([-1, RESOLUTION, RESOLUTION, 3])

def convertPredictionsToCsv(predictions, files, path_to_csv):
    print("Writing to csv...")
    df = pd.DataFrame(data=None, index=None, columns=columns, dtype=None, copy=False)
    size = len(predictions)
    for i in range(size):
        df.loc[i] = [files[i]] + predictions[i]
    df.to_csv(path_to_csv, index=False)
    print("Done.")
    return df

def convertPredictionsArrayToLabels(predictions):
    res = []
    for prediction in predictions:
        subres = []
        for i in range(0, prediction.size):
            if prediction[i] == 1:
                subres.append(columns[i+1])
        res.append(subres)
    return res

class Manager:
    
    def __init__(self):
        self.csv_data = None
        pass
    
    def initializeModel(self):
        
        print("Loading base model...")
        self.base_model = keras.applications.ResNet50(include_top=False, pooling='avg', input_shape=(RESOLUTION, RESOLUTION, 3))
        self.base_model.trainable = False
        print("Creating model...")
        
        self.model = keras.Sequential()
        self.model.add(self.base_model)
        self.model.add(layers.Dense(38, activation='sigmoid'))
        
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=[keras.metrics.BinaryAccuracy()])
        
        print("Model compiled")
    
    def loadCsv(self, train_path = csv_train_path, test_path = csv_test_path):
        print("Loading csv...")
        train = pd.read_csv(train_path)
        test = pd.read_csv(test_path)
        self.names_train = train["Name"]
        self.names_test = test["Name"]
        self.all_image_names = pd.concat([self.names_test, self.names_train], ignore_index=True)
        self.y_train = train.drop(columns=["Name"]).to_numpy().reshape([-1, 38]) * 1
        self.y_test = test.drop(columns=["Name"]).to_numpy().reshape([-1, 38]) * 1
        self.labels = test.columns[1:]
        print("Done")
      
    
    def importTrainingDataFromBinaryFile(self, path_to_file = bin_photos_path):
        print("Importing images from binary file...")
        self.x_train = np.fromfile(path_to_file, dtype=np.uint8).reshape([-1, RESOLUTION, RESOLUTION, 3])
        self.x_test = self.x_train[0:(self.names_test.size)]
        self.x_train = self.x_train[(self.names_test.size):]
        print("Done")
    
    def train(self, epochs):
        print("Training...")
        self.model.fit(self.x_train, self.y_train, verbose = 1, epochs = epochs)
        print("Done")
    def test(self):
        print("Testing...")
        self.model.evaluate(self.x_test, self.y_test)
        print("Done")
    def saveModel(self, name):
        print("Saving model...")
        self.model.save(os.path.join(models_path, name))
        print("Done")
    def loadModel(self, name):
        print("Loading model...")
        self.model = keras.models.load_model(os.path.join(models_path, name))
        print("Done")
    
    def getPredictionsArray(self, images_path = live_test_path, binary_path = None):
        print("Predicting....")
        files = [file for file in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, file))]           
        images = None
        if binary_path != None:
            images = importImagesFromBinaryFile(images_path)
        else:
            filepaths = [os.path.join(images_path, filename) for filename in files]
            images = proccessAllImages(filepaths)
            
        predictions_raw = self.model.predict(images, verbose = 1)
        predictions = [ [( 1 if prediction >= 0.5 else 0) for prediction in prediction_run ] for prediction_run in predictions_raw]
        print("Done.")
        return (predictions, files)
    
    def predictAndSaveToCsv(self, images_path = live_test_path, binary_path = None, path_to_csv = os.path.join(training_data_folder, "result.csv")):
        predictions, files = self.getPredictionsArray(images_path, binary_path)
        return convertPredictionsToCsv(predictions, files, path_to_csv)

"""

cb_early_stopper = EarlyStopping(monitor='val_loss', patience=EARLY_STOP_PATIENCE)
cb_checkpointer = ModelCheckpoint(filepath='../models/trained_models/best2.hdf5', monitor='val_loss',
                                  save_best_only=True, mode='auto')

image_size = IMAGE_RESIZE
data_generator = ImageDataGenerator(preprocessing_function=preprocess_input)

train_generator = data_generator.flow_from_directory(
    '../data/train_clean_dataset',
    target_size=(image_size, image_size),
    batch_size=BATCH_SIZE_TRAINING,
    class_mode='categorical')

validation_generator = data_generator.flow_from_directory(
    '../data/val_clean_dataset',
    target_size=(image_size, image_size),
    batch_size=BATCH_SIZE_VALIDATION,
    class_mode='categorical')

fit_history = model.fit_generator(
    train_generator,
    steps_per_epoch=STEPS_PER_EPOCH_TRAINING,
    epochs=NUM_EPOCHS,
    validation_data=validation_generator,
    validation_steps=STEPS_PER_EPOCH_VALIDATION,
    callbacks=[cb_checkpointer, cb_early_stopper]
)

"""