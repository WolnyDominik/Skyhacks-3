from model_manager import *
import os

#os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# physical_devices = tf.config.experimental.list_physical_devices('GPU')
# assert len(physical_devices) > 0, "Not enough GPU hardware devices available"
# config = tf.config.experimental.set_memory_growth(physical_devices[0], True)


# exit()

#najpierw ustawić scierzki wszystkie

#step = 1
#film_name = 'czesto.mp4'
#czesto_path = os.path.join(film_data_folder, "czesto")

#manager = Manager()
#manager.loadCsv()

#import time

#start = time.time()

#film_to_frames(film_name, step=step)


#processAllImagesToBinary(images_path=czesto_path, bin_path=film_bin_path) # to wywołać tylko i wyłącznie raz
#manager.importTrainingDataFromBinaryFile(path_to_file=film_bin_path)
# manager.initializeModel2()
#manager.loadModel("wygwywamy.h5")
# exit()
#manager.predictAndSaveToCsv(binary_path=live_test_bin_path, treshold = 0.2)

# manager.train(2)
#manager.test()

#manager.loadEnsamble('ens', count = 5)
#manager.trainEnsamble(5)
#manager.testEnsamble()

#manager.loadModel('to-dalej-przegrywamy.h5')
# manager.trainSmart("smartv2", 2000, max_last_improved=20)
# manager.saveModel('smartv2/last.h5')
#manager.predictAndSaveToCsv(
#    images_path=czesto_path,
#    binary_path=film_bin_path, 
#    path_to_csv=os.path.join(film_data_folder, "film.csv"), 
#    treshold = 0.2)

#process_film_csv(jump=step, treshold=2)


manager = Manager()
manager.loadCsv()
manager.importTrainingDataFromBinaryFile()
manager.loadMultimodel("multimodel1/krzeslo")
manager.predictMultimodelAndSaveToCsv()
#manager.testMultimodel()
"""
manager.testMultimodel()
manager.trainMultimodel(2)
manager.testMultimodel()
manager.saveMultimodel("multimodel1/krzeslo")
"""