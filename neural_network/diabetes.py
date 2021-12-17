"""
Autorzy: Klaudia Pardo, Martyna Klebba

Wykrywanie cukrzycy

Reguirements:
pip install tensorflow
pip install numpy
pip install sklearn
"""

import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow import keras


class DiabetesNeuralNetwork():
    def __init__(self):
        """
        Wytworzenie początkowego atrybutu modelu. Wykonanie metody prepare data.
        """
        self.model = None
        self.prepare_data()

    def prepare_data(self):
        """
        Wczytuje dane, wstępnie je przetwarza i dzieli na zbiór treningowy i testowy.
        Returns
        -------
        None
        """
        f = open("diabetes.csv")
        data = np.genfromtxt(fname=f, delimiter=',')
        X = data[:, :-1]
        y = data[:, -1]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.3)

    def train_model(self):
        self.prepare_neural_network_model()
        self.compile_fit()
        self.evaluate()

    def prepare_neural_network_model(self):
        """
        Przygotowuje model, tworzy warstwy.
        Returns
        -------
        None
        """
        self.model = keras.models.Sequential()
        self.model.add(keras.layers.Input(8))
        self.model.add(keras.layers.Dense(6, activation='relu'))
        self.model.add(keras.layers.Dense(1, activation='sigmoid'))

    def compile_fit(self):
        """
        Kompiluje i trenuje model.
        Returns
        -------
        None
        """
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        self.model.fit(self.X_train, self.y_train, epochs=1000, batch_size=32)

    def evaluate(self):
        """
        Drukuje wartości strat i dokładności dla zbiorów treningowych i testowych.
        Returns
        -------
        None
        """
        print('Evaluating pima indians neural network...')
        loss, accuracy = self.model.evaluate(self.X_train, self.y_train)
        print('Train Loss:, %.2f' % (loss * 100))
        print('Train Accuracy: %.2f' % (accuracy * 100))
        print('---------------------------------------')
        loss, accuracy = self.model.evaluate(self.X_test, self.y_test)
        print('Test Loss:, %.2f' % (loss * 100))
        print('Test Accuracy: %.2f' % (accuracy * 100))


diabetes = DiabetesNeuralNetwork()
diabetes.train_model()