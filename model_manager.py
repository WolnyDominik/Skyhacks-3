from os import name
import tensorflow as tf
from tensorflow.python.keras.backend import print_tensor
# import tensorflow_addons as tfa
keras = tf.keras
layers = keras.layers

import pandas as pd
import os
import math
import cv2
import numpy as np
from pathlib import Path
import glob
import altair as alt
from altair_saver import save

alt.renderers.enable('svg')#'altair_saver', ['vega-lite', 'svg'])
#alt.renderers.enable('mimetype')


#from keras.applications.resnet50 import preprocess_input
#from keras.preprocessing.image import ImageDataGenerator

training_data_folder = r"."
film_data_folder = os.path.join(training_data_folder, "films")
csv_path = os.path.join(training_data_folder, "training_labels.csv")
csv_test_path = os.path.join(training_data_folder, "training_labels_test.csv")
csv_train_path = os.path.join(training_data_folder, "training_labels_train.csv")
photos_path = os.path.join(training_data_folder, "training_images")
bin_photos_path = os.path.join(training_data_folder, "training_images.bin")
models_path = os.path.join(training_data_folder, "models")
live_test_path = os.path.join(training_data_folder, "live_test_images")
live_test_bin_path = os.path.join(training_data_folder, "live_test.bin")
film_bin_path = os.path.join(film_data_folder, "film.bin")

RESOLUTION = 224
USE_LOGITS = False


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
    print(names_list)
    # if names_list == None:
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
        df.loc[i] = [files[i]] + [int(x) for x in predictions[i]]
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


def film_to_frames(filename: str, path=film_data_folder, step:float=1):
    print('Start conversion')
    idx = filename.rfind('.')
    movie_name = filename[:idx]

    movie = cv2.VideoCapture(filename)
    opened = movie.isOpened
    
    if not opened:
        print(f'Error reading {filename}')
        return
    
    framerate = movie.get(cv2.CAP_PROP_FPS)
    framestep = math.floor(framerate*step)
    cap = framerate * 30
    fps = 0
    target_folder = os.path.join(path, 'czesto')

    os.makedirs(target_folder, exist_ok=True)
    files = glob.glob(target_folder+'/*')
    
    for f in files:
        os.remove(f)

    while opened:
        if fps > cap:
            break
        ret, frame = movie.read()
        if ret == True:
            if fps % framestep == 0:
                cv2.imwrite(target_folder+f'/{int(fps/framestep)}.jpg', frame)
            fps += 1
        else:
            break
    
    movie.release()
    print('End conversion')


def process_film_csv(csv_path: str=os.path.join(film_data_folder, "film.csv"), jump: float=1, treshold: int=0):
    df = pd.read_csv(csv_path)
    columns = df.columns.tolist()[1:]
    
    stats = {col: 0 for col in columns}
    conts = {col: 0 for col in columns}
    tresh = {col: treshold for col in columns}
    names = df['Name'].tolist()
    
    times = [float(name[:name.rfind('.')])*jump for name in names]
    df['time'] = times
    df = df.sort_values(by='time', ascending=True)
    
    started = {}
    ended = []
    
    for _, row in df.iterrows():
        for col in columns:
            if row[col] and not conts[col]:
                started[col] = {
                    'class': col,
                    'xp': row['time'],
                    'xk': 0
                }
                stats[col] += 1
                conts[col] =  1
                tresh[col] =  treshold

            elif not row[col] and tresh[col] and conts[col]:
                tresh[col] -= 1

            elif not row[col] and not tresh[col] and conts[col]:
                conts[col] = 0
                started[col]['xk'] = prev_row['time']
                ended.append(started[col])
        
        prev_row = row

    for col in started:
        if started[col]:
            if not started[col]['xk']:
                started[col]['xk'] = prev_row['time']
                ended.append(started[col])

    chart = alt.Chart(pd.DataFrame(ended)).mark_bar(height=10, color="rgb(200,100,0)").encode(
        alt.X('xp', title=''),
        alt.X2('xk',title=''),
        alt.Y('class',title='')
    ).configure(
        background="#202020",    
    ).configure_axis(
        labelColor="#ffffff"
    )
    
    save(chart,'film.html')


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
    
    def initializeMultiModel(self):
        
        print("Loading base model...")
        self.base_model = keras.applications.ResNet50(include_top=False, pooling='avg', input_shape=(RESOLUTION, RESOLUTION, 3))
        self.base_model.trainable = False
        print("Creating models...")
        
        self.multimodel = [None] * 38;
        
        for i in range(len(self.multimodel)):
            
            print("Creating model nr ", i)
            
            self.multimodel[i] = keras.Sequential()
            self.multimodel[i].add(self.base_model)
            self.multimodel[i].add(layers.Dense(2, activation='softmax'))
            
            self.multimodel[i].compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=["acc"])
        
        print("Models compiled")
    
    
    def initializeEnsamble(self, count):
        print("Loading base model...")
        self.base_model = keras.applications.ResNet50(include_top=False, pooling='avg', input_shape=(RESOLUTION, RESOLUTION, 3))
        self.base_model.trainable = False
        print("Creating models...")
        self.ensamble = [ None ] * count
        for i in range(count):
            print("Creating model nr. ", i)
            self.ensamble[i] = keras.Sequential()
            self.ensamble[i].add(self.base_model)
            self.ensamble[i].add(layers.Dense(38, activation='sigmoid'))
            self.ensamble[i].compile(optimizer='adam', loss=keras.losses.BinaryCrossentropy(from_logits=USE_LOGITS), metrics=[keras.metrics.BinaryAccuracy()])
        print("Ensamble compiled")
    
    
    def initializeModel2(self):
        
        print("Loading base model...")
        self.base_model = keras.applications.ResNet50(include_top=False, pooling='avg', input_shape=(RESOLUTION, RESOLUTION, 3))
        self.base_model.trainable = False
        print("Creating model...")
        
        self.model = keras.Sequential()
        self.model.add(self.base_model)
        self.model.add(layers.Dense(38, activation='sigmoid'))
        
        #optimizer = tfa.optimizers.RectifiedAdam()
        optimizer = keras.optimizers.Adam(learning_rate=0.00004)
        loss = keras.losses.BinaryCrossentropy(from_logits=USE_LOGITS)
        metrics=[keras.metrics.BinaryAccuracy()]
        self.model.compile(optimizer=optimizer, loss=loss, metrics = metrics)
        
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
    
    
    def trainSmart(self, name, maxepochs=50, epoch_step = 1, max_last_improved = 10):
        last = self.test(verbose = 0)
        last_improved = 0
        for i in range (maxepochs):
            print("  ", i, " / ", maxepochs, "  (last improved: ", last_improved, ") ...")
            self.train(epoch_step, verbose = 0)
            test = self.test(verbose = 0)
            if test[0] < last[0]:
                if test[1] >= last[1]:
                    print("New best: ", test, last)
                    last = test
                    self.saveModel(os.path.join(name, "best.h5"), overwrite=True)
                else:
                    print("New loss: ", test, last)
                    last[0] = test[0]
                    self.saveModel(os.path.join(name, "best-loss.h5"), overwrite=True)
                last_improved = 0
            elif test[1] > last[1]:
                print("New acc:  ", test, last)
                last[1] = test[1]
                self.saveModel(os.path.join(name, "best-acc.h5"), overwrite=True)
                last_improved = 0
            else:
                last_improved += 1
            if last_improved >= max_last_improved:
                last_improved = 0
                self.loadModel(os.path.join(name, "best.h5"))
    
    
    def train(self, epochs, verbose = 1):
        if verbose > 0:
            print("Training...")
        return self.model.fit(self.x_train, self.y_train, verbose = verbose, epochs = epochs)
        if verbose > 0:
            print("Done.")
            
            
    def trainMultimodel(self, epochs, verbose = 1):
        if verbose > 0:
            print("Training...")
        for i in range(38):
            self.multimodel[i].fit(self.x_train, self.y_train[:,i], verbose = verbose, epochs = epochs)
        if verbose > 0:
            print("Done.")
    
    
    def trainEnsamble(self, epochs, verbose = 1):
        if verbose > 0:
            print("Training...")
        for i in range(len(self.ensamble)):
            if verbose > 0:
                print("Model nr", i)
            self.ensamble[i].fit(self.x_train, self.y_train, verbose = verbose, epochs = epochs)
        if verbose > 0:
            print("Done.")
        
    
    def test(self, verbose = 1):
        if verbose > 0:
            print("Testing...")
        return self.model.evaluate(self.x_test, self.y_test, verbose = verbose)
        if verbose > 0:
            print("Done.")
            
    
    def testMultimodel(self, verbose = 1):
        if verbose > 0:
            print("Testing...")
        results = [None] * 38
        for i in range(38):
          results[i] = self.multimodel[i].evaluate(self.x_test, self.y_test[:,i], verbose = verbose)
        if verbose > 0:
            for i in range(38):
                print(columns[i+1], ": ", results[i])
            print("Done.")
    
    
    def testEnsamble(self, verbose = 1, treshold = 0.5):
        if verbose > 0:
            print("Testing...")
        predictions = self.getEnsamblePredictionsFromData(self.x_test, treshold, verbose)
        res_loss = np.mean(keras.losses.binary_crossentropy(self.y_test, predictions, from_logits=USE_LOGITS))
        res_acc = np.mean(keras.metrics.binary_accuracy(self.y_test, predictions))
        if verbose > 0:
            print("Loss: ", res_loss, "  Acc: ", res_acc)
            print("Done.")
        return [res_loss, res_acc]
    
    
    def saveModel(self, name, overwrite = False):
        print("Saving model...")
        self.model.save(os.path.join(models_path, name), overwrite=overwrite)
        print("Done")
    
    
    def loadModel(self, name):
        print("Loading model...")
        self.model = keras.models.load_model(os.path.join(models_path, name))
        print("Done")
        
    
    def saveEnsamble(self, name, overwrite = False):
        print("Saving ensamble...")
        for i in range(len(self.ensamble)):
            self.ensamble[i].save(os.path.join(models_path, name + str(i) +'.h5'), overwrite=overwrite)
        print("Done")
    
    
    def loadEnsamble(self, name, count):
        print("Loading ensamble...")
        self.ensamble = [None] * count
        for i in range(count):
            print("Loading model nr ", i)
            self.ensamble[i] = keras.models.load_model(os.path.join(models_path, name + str(i) +'.h5'))
        print("Done")
    
    def saveMultimodel(self, name, overwrite = False):
        print("Saving multimodel...")
        for i in range(38):
            print("Saving multimodel ", i, " / 38")
            self.multimodel[i].save(os.path.join(models_path, name + str(i) +'.h5'), overwrite=overwrite)
        print("Done")
    
    
    def loadMultimodel(self, name):
        print("Loading multimodel...")
        self.multimodel = [None] * 38
        for i in range(38):
            print("Loading model nr ", i)
            self.multimodel[i] = keras.models.load_model(os.path.join(models_path, name + str(i) +'.h5'))
        print("Done")
    
    
    def getEnsamblePredictionsFromData(self, data, treshold = 0.5, verbose = 1):
        results = np.zeros(shape=[data.shape[0], 38])
        for i in range(len(self.ensamble)):
            if verbose > 0:
                print("Model nr", i)
            predictions_raw = self.ensamble[i].predict(data, verbose = verbose)
            results_to_add = [ [( 1 if prediction >= treshold else 0) for prediction in prediction_run ] for prediction_run in predictions_raw]
            results_to_add = np.array(results_to_add)
            results += results_to_add
        return results / len(self.ensamble)
    
    
    def getPredictionsArray(self, images_path = live_test_path, binary_path = None, treshold = 0.5):
        print("Predicting....")
        files = [file for file in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, file))]           
        images = None
        if binary_path != None:
            images = importImagesFromBinaryFile(binary_path)
        else:
            filepaths = [os.path.join(images_path, filename) for filename in files]
            images = proccessAllImages(filepaths)
            
        predictions_raw = self.model.predict(images, verbose = 1)
        predictions = [ [( 1 if prediction >= treshold else 0) for prediction in prediction_run ] for prediction_run in predictions_raw]
        print("Done.")
        return (predictions, files)
    
    def getMultimodelPredictionsArray(self, images_path = live_test_path, binary_path = None):
        print("Predicting....")
        files = [file for file in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, file))]           
        images = None
        if binary_path != None:
            images = importImagesFromBinaryFile(binary_path)
        else:
            filepaths = [os.path.join(images_path, filename) for filename in files]
            images = proccessAllImages(filepaths)
        
        size = images.shape[0]
        predictions = np.empty(shape = [size, 38])
        for i in range(38):
            print("Predicting model nr ", i)
            prediction_row = self.multimodel[i].predict(images, verbose = 1)
            predictions[:, i] = [int(pred[1]>pred[0]) for pred in prediction_row]
        
        print("Done.")
        return (predictions, files)
    
    
    def getEnsamblePredictionsArray(self, images_path = live_test_path, binary_path = None, treshold = 0.5):
        print("Predicting....")
        files = [file for file in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, file))]           
        images = None
        if binary_path != None:
            images = importImagesFromBinaryFile(binary_path)
        else:
            filepaths = [os.path.join(images_path, filename) for filename in files]
            images = proccessAllImages(filepaths)
            
        predictions_raw = self.getEnsamblePredictionsFromData(images, treshold = treshold)
        predictions = [ [( 1 if prediction >= 0.5 else 0) for prediction in prediction_run ] for prediction_run in predictions_raw]
        
        print("Done.")
        return (predictions, files)
    
    
    def predictAndSaveToCsv(self, images_path = live_test_path, binary_path = live_test_bin_path, path_to_csv = os.path.join(training_data_folder, "result.csv"), treshold=0.5):
        predictions, files = self.getPredictionsArray(images_path, binary_path, treshold)
        return convertPredictionsToCsv(predictions, files, path_to_csv)
    
    
    def predictEnsambleAndSaveToCsv(self, images_path = live_test_path, binary_path = live_test_bin_path, path_to_csv = os.path.join(training_data_folder, "result.csv"), treshold=0.5):
        predictions, files = self.getEnsamblePredictionsArray(images_path, binary_path, treshold)
        return convertPredictionsToCsv(predictions, files, path_to_csv)

    
    def predictMultimodelAndSaveToCsv(self, images_path = live_test_path, binary_path = live_test_bin_path, path_to_csv = os.path.join(training_data_folder, "result.csv")):
        predictions, files = self.getMultimodelPredictionsArray(images_path, binary_path)
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