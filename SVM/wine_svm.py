"""
Autorzy: Martyna Klebba, Klaudia Pardo

Klasyfikacja danych analizy chemicznej win

Source:
https://www.youtube.com/watch?v=p_rmpE0XwCc

Requirements:
pip install pandas
pip install sklearn
pip install scikit-learn

"""
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.datasets import load_wine

#załadowanie danych
wines = load_wine()
#print(wines['DESCR'])

#Przypisanie kolumn do zmiennych
X, y = wines['data'], wines['target']

"""
Podział danych na dane testowe oraz treningowe
"""
#średnia ze zmiennej wynosi 0 a dla niestandardowej 1
scaler = StandardScaler()
#SVC klasyfikator
svm = SVC(C=1e-2, kernel='linear', degree=2)
#transformacja danych
X = scaler.fit(X).transform(X)

#Podział danych na dane testowe oraz treningowe
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

#Prognozowanie klasy na podstawie danych
y_pred = svm.fit(X_train, y_train).predict(X_test)


print(f"""{
classification_report(y_pred, y_test)}
""")