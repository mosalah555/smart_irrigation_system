from raspberry.ml.inference import preprocess, predict_irrigation
print(predict_irrigation(preprocess(32.4, 31.8, 0.0)))
