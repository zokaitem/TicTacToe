import random
from lenta import sukurti_lenta, vaizduoti_lenta
from ejimas import ejimas
from laimejimas import laimejimas

def main():
    zaidejas1 = 0
    zaidejas2 = 0

    while True:
        lenta = sukurti_lenta()
        dabar_zaidzia = random.choice(['X', 'O'])

        while True:
            vaizduoti_lenta(lenta)
            move = ejimas(lenta, dabar_zaidzia)
            lenta[move] = dabar_zaidzia
            laimetojas = laimejimas(lenta)
            if laimetojas:
                vaizduoti_lenta(lenta)
                print(f"Žaidėjas {dabar_zaidzia} laimėjo 🧠! Konkurente, per kitą partiją nemiegok!")

                if dabar_zaidzia == "X":
                    zaidejas1 += 1
                elif dabar_zaidzia == "O":
                    zaidejas2 += 1
                print(f"Žaidėjo X taškai: {zaidejas1}, Žaidėjo O taškai: {zaidejas2}")

                break
            elif '_' not in lenta:
                vaizduoti_lenta(lenta)
                print("Lygiosios!🙌🏼")
                break
            dabar_zaidzia = 'O' if dabar_zaidzia == 'X' else 'X'

        restart = input("Ar norite bandyti dar kartą? (taip/ne): ").lower()
        if restart == "taip":
            dabar_zaidzia = random.choice(['X', 'O'])
        else:
            print("Iki kito karto, žaidėjai!")
            break

if __name__ == "__main__":
    main()