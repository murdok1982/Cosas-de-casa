
import tensorflow as tf
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


datosHistoricosEuro = pd.read_csv("Euro.csv")

NumerosProbables = datosHistoricosEuro.iloc['Euro']

model=tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units=1,input_shape=[1]))

# model.summary()
model.compile(optimizer=tf.keras.optimizers.Adam(0.5)loss='mean_squared_error')

epochs_hist = model.fit(NumerosProbables,epochs=5000)


print(NumerosProbables)




