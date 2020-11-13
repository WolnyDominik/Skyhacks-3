from model_manager import *

#najpierw ustawić scierzki wszystkie

manager = Manager()
manager.loadCsv()
#manager.processAllImagesToBinary(manager.all_image_names.to_numpy()) # to wywołać tylko i wyłącznie raz
manager.importTrainingDataFromBinaryFile()

manager.loadModel("wygwywamy.h5")

manager.train(2)
manager.test()
