import random

def interrogare_alunni(alunni, quanti):
    if quanti < 1 or quanti > len(alunni):
        print("Inserisci un numero compreso tra 1 e", len(alunni))
        return

    try:
        with open("alunni_interrogati.txt", "r") as file:
            alunni_interrogati = file.read().splitlines()
    except FileNotFoundError:
        alunni_interrogati = []

    alunni_disponibili = [alunno for alunno in alunni if alunno not in alunni_interrogati]

    if not alunni_disponibili:
        print("Hai interrogato tutti gli alunni disponibili.")
        return

    alunni_selezionati = random.sample(alunni_disponibili, quanti)

    print("Gli alunni interrogati sono:")
    for alunno in alunni_selezionati:
        print(alunno)

    with open("alunni_interrogati.txt", "a") as file:
        for alunno in alunni_selezionati:
            file.write(alunno + "\n")

alunni = [
    "corrado",
    "benny",
    "erika"
]

nalunni = int(input("Quanti alunni vuoi interrogare?"))
interrogare_alunni(alunni, nalunni)
