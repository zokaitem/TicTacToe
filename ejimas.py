
def ejimas(lenta, simbolis):
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


