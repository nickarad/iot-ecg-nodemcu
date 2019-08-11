import pandas as pd 
import numpy as np
import ecg_plot as pl
import tensorflow as tf 
from sklearn import preprocessing

data = pd.read_csv("ecg.csv") 
# data.index.to_numpy()
# print(data)
# print(type(data))
# print(data['clintellimqtt_consumer.value'].to_numpy())
ecg = data['clintellimqtt_consumer.value'].to_numpy()
ecg = (ecg * 3.3)/1024
# ecg = tf.keras.utils.normalize(ecg, axis = 1)
# ecg.reshape(-1,1322)
# ecg = tf.keras.utils.normalize(ecg, axis = 1)
# ecg_normalized = preprocessing.normalize(ecg, norm='l2')
print(ecg)
print(ecg.size)
print(ecg.shape)
# print(ecg_normalized)
pl.ecg_plot(ecg)

