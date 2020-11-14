from model_manager import *

#najpierw ustawić scierzki wszystkie

manager = Manager()
manager.loadCsv()
#processAllImagesToBinary(manager.all_image_names.to_numpy()) # to wywołać tylko i wyłącznie raz
manager.importTrainingDataFromBinaryFile()
#manager.initializeModel2()
#manager.loadModel("wygwywamy.h5")

#manager.predictAndSaveToCsv(binary_path=live_test_bin_path, treshold = 0.2)

#manager.train(2)
#manager.test()

#manager.trainSmart("smartv2", 2000, max_last_improved=20)
#manager.saveModel('smartv2\\last.h5')
manager.loadModel('smartv2\\best.h5')
#manager.predictAndSaveToCsv(binary_path=live_test_bin_path, path_to_csv = os.path.join(training_data_folder, "smartv1.csv"), treshold = 0.2)