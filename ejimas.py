
def ejimas(lenta, simbolis):
    """
    Prašo žaidėjo įvesti skaičių, atitinkantį jo ėjimą;
    patikrina, ar pasirinktas langelis užimtas ir prašo įvesti kitą pasirinkimą, jei taip;
    priima parametrus lenta ir simbolis:
    :param lenta: dabartinė žaidimo lenta, kuri parodo, kurios pozicijos jau užimtos;
    :param simbolis: žaidėjo, kuris atlieka ėjimą, simbolis (X arba O);
    :return: lentos indeksas, atitinkantis žaidėjo pasirinktą ėjimą.
    """
    while True:
        try:
            eiti = int(input(f"Žaidėjau {simbolis}, įveskite skaičių nuo 1 iki 9: "))
            if eiti < 1 or eiti > 9:
                print("Pasirinkite skaičių nuo 1 iki 9.")
                continue
            index = eiti - 1

            if lenta[index] != '_':
                print("Langelis užimtas, rinkitės kitą.")
                continue
            return index
        except ValueError:
            print("Klaida, įveskite skaičių nuo 1 iki 9.")


