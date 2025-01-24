
def laimejimas(lenta):
    """
    funkcija tikrina, ar vienas iš žaidėjų laimėjo
    :param lenta: žaidimo lenta, kurioje yra 9 langeliai, kiekvienas gali būti užpildytas
    simboliu 'X' arba 'O', arba būti tuščias
    :return: jei randama laiminti kombinacija, grąžinamas laimėtojo simbolis 'X' arba 'Y;
    jei laiminti kombinacija nerandama grąžinama 'None';
    """
    kombinacijos =[[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for kombinacija in kombinacijos:
        if lenta[kombinacija[0]] == lenta[kombinacija[1]] == lenta[kombinacija[2]] != '_':
            return lenta[kombinacija[0]]
