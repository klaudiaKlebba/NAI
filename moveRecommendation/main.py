'''
Autorzy: Klaudia Pardo, Martyna Klebba

Program rekomendacji filmów i seriali, który proponuje danemu użytkowniki polecane filmy/seriale oraz takich, które mogą mu się nie spodobać.

Requirements:
pip install numpy
'''
import json
import numpy as np


def euclidean_score(dataset, first_user, second_user):
    """Metoda wylicza odległość jaka jest między pierwszym użytkownikiem a drugim
    Parametry wejściowe:
        dataset (dict): Zaimportowane dane użytkowników
        user1 (str): Pierwszy użytkownik
        user2 (str): Drugi użytkownik
    Parametry zwracane:
        float: Odległość między użytkownikami
    """
    if first_user not in dataset:
        raise TypeError('Nie można znaleść użytkownika :' + first_user)

    if second_user not in dataset:
        raise TypeError('Nie można znaleść użytkownika :' + second_user)

    common_movies = {}

    for item in dataset[first_user]:
        if item in dataset[second_user]:
            common_movies[item] = 1

    # jeśli użtkownicy nie mają wspólnych filmów wtedy zwraca 0
    if len(common_movies) == 0:
        return 0

    squared_diff = []

    for item in dataset[first_user]:
        if item in dataset[second_user]:
            squared_diff.append(np.square(dataset[first_user][item] - dataset[second_user][item]))

    return 1 / (1 + np.sqrt(np.sum(squared_diff)))


def print_result(user_name, user_dict):
    """
    Matoda wyświetla 5 najlepszych filmów i 5 najgorszych według oceny użytkownika
    :param user_name: Nazwa użytkownika
    :param user_dict: dane użytkownika, który miał najwyższą wartość w przeliczeniu odległości
    :return: Zwracana jest lista z poleconymi i nie polecanymi filmami
    """
    print('Wybrano ' + user_name)
    movie_without_duplicates = {}
    for key, value in user_dict.items():
        if key not in data[user].keys():
            movie_without_duplicates[key] = value
    # sortowanie filmów niepowtarzających się po ocenie filmów, czyli od najwyższej do najniższej oceny
    sorted_dict = dict(sorted(movie_without_duplicates.items(), key=lambda element: element[1], reverse=True))
    # List Slicing: list[start:stop:step]
    best5 = dict(list(sorted_dict.items())[:5])
    worse5 = dict(list(sorted_dict.items())[-5:])
    counter = 0
    movie_all = []

    #dodawanie do tablicy
    print('\nPolecane filmy:')
    for item in best5:
        print('[' + str(counter) + '] ' + item + ' ' + str(best5[item]))
        counter += 1
        movie_all.append(item)

    print('\nNie polecane filmy:')
    for item in worse5:
        print('[' + str(counter) + '] ' + item + ' ' + str(worse5[item]))
        counter += 1
        movie_all.append(item)
    return movie_all


def select_user():
    """
    Metoda służąca do wyboru użytkownika sposród listy dostępnych
    :return: Nazwa wybranego użytkownika
    """
    counter = 0
    user_list = []
    print('\nWybierz osobe:')
    #tworzymy liste z użytkownikami
    for item in data:
        print('[' + str(counter) + '] ' + item)
        user_list.append(item)
        counter += 1
    return user_list[int(input())]


if __name__ == '__main__':
    json_file = 'filmy.json'
    with open(json_file, encoding='utf-8') as file:
        data = json.loads(file.read())

    user = select_user()
    score_array = []

    #przeszukujemy plik z danymi.
    #Jak drugi użtkownik jest różny od tego którego wybraliśmy to wyliczamy odległośc miedzy naszym wybranym a drugim użytkownikiem.
    #Potem dodajemy do tablicy
    for item in data:
        if item != user:
            score_array.append({'score': euclidean_score(data, user, item), 'user': item})

    #z tablicy score_array bierzemy użytkownika z najwyższą wartością
    max_score = max(score_array, key=lambda x: x['score'])
    #do wybranej wartości bierzemy przypisanego użytkownika
    user_movies = data[max_score['user']]
    #wyświetlamy 5 najlepszych i 5 najgorszych filmów
    movie_all_list = print_result(max_score['user'], user_movies)