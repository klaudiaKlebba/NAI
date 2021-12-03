"""
Autorzy: Martyna Klebba, Klaudia Pardo

Klasyfikacja danych o cykrzycy

Source:
https://www.youtube.com/watch?v=p_rmpE0XwCc

Requirements:
pip install pandas
pip install sklearn
pip install scikit-learn

"""
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix


#załadowanie danych
data = pd.read_csv("https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv",
                   delimiter=',')
dataset = data.values

#Przypisanie kolumn do zmiennych
X, y = dataset[:, :-1], dataset[:, -1]

#średnia ze zmiennej wynosi 0 a dla niestandardowej 1
scaler = StandardScaler()


#SVC klasyfikator
svm = SVC(C=1e-2, kernel='linear', gamma=4)

#transformacja danych
X = scaler.fit(X).transform(X)

#Podział danych na dane testowe oraz treningowe
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.50)

#Prognozowanie klasy na podstawie danych
y_pred = svm.fit(X_train, y_train).predict(X_test)


print(f"""{
classification_report(y_pred, y_test)}
""")




