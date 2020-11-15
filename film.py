import sys
from model_manager import *
import os

step = 0.25
film_name = sys.argv[1]
film_folder= sys.argv[2]
czesto_path = os.path.join(film_data_folder, 'czesto')

manager = Manager()
manager.loadCsv()

film_to_frames(film_name, step=step)

processAllImagesToBinary(images_path=czesto_path, bin_path=film_bin_path) # to wywołać tylko i wyłącznie raz
manager.importTrainingDataFromBinaryFile(path_to_file=film_bin_path)

#manager.loadModel('to-dalej-przegrywamy.h5')
manager.loadModel('wygwywamy.h5')

manager.predictAndSaveToCsv(
    images_path=czesto_path,
    binary_path=film_bin_path, 
    path_to_csv=os.path.join(film_data_folder, "film.csv"), 
    treshold = 0.2)

process_film_csv(jump=step, treshold=1,film_folder=film_folder)
