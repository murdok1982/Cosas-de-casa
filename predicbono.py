import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

def predict_next_vector(file_path, method):
    data = pd.read_csv(file_path)
    data = np.array(data)
    # Divide los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(data[:,:-1], data[:,-1], test_size=0.2)
    if method == "mean":
        # Devuelve un vector probable siguiente basado en la media de los vectores anteriores
        next_vector = np.mean(data, axis=0)
    elif method == "linear_regression":
        # Entrena un modelo de regresión lineal con los vectores anteriores
        model = LinearRegression()
        model.fit(X_train, y_train)
        # Utiliza el modelo para predecir el siguiente vector
        next_vector = model.predict(X_test)
    elif method == "random_forest":
        # Entrena un modelo de bosque aleatorio con los vectores anteriores
        model = RandomForestRegressor()
        model.fit(X_train, y_train)
        # Utiliza el modelo para predecir el siguiente vector
        next_vector = model.predict(X_test)
    elif method == "svr":
        # Entrena un modelo de support vector regression con los vectores anteriores
        model = SVR()
        model.fit(X_train, y_train)
        # Utiliza el modelo para predecir el siguiente vector
        next_vector = model.predict(X_test)
    else:
        raise ValueError("Método no válido. Los métodos disponibles son: 'mean', 'linear_regression', 'random_forest' y 'svr'")
    return next_vector
    #Imprime el menu de opciones
print("Selecciona una opción:")
print("1. Método de la media")
print("2. Regresión lineal")
print("3. Bosque aleatorio")
print("4. Support Vector Regression")

#Pide al usuario la opción deseada
selected_option = input()

#Selecciona el método de acuerdo a la opción elegida
if selected_option == "1":
    method = "mean"
elif selected_option == "2":
    method = "linear_regression"
elif selected_option == "3":
    method = "random_forest"
elif selected_option == "4":
    method = "svr"
else:
    raise ValueError("Opción no válida. Selecciona una opción válida")

#Pide la ruta del archivo
file_path = input("Ingresa la ruta del archivo a leer: (C:\Users\gustavo\Desktop\programa bonoloto)")

#Llama a la función predict_next_vector con el método y la ruta del archivo elegidos
next_vector = predict_next_vector(file_path, method)

#Imprime el vector probable siguiente
print("Vector probable siguiente:", next_vector)

for i in range(len(next_vector)):
    print("Elemento ",i," del vector probable siguiente:", next_vector[i])
