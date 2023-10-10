import os
import random

def interrogare_alunni(classe, quanti):
    folder_path = "classi"
    filename_alunni = os.path.join(folder_path, f"alunni_{classe}.txt")
    filename_interrogati = os.path.join(folder_path, f"alunni_interrogati_{classe}.txt")

    try:
        with open(filename_alunni, "r") as file:
            alunni = file.read().splitlines()
    except FileNotFoundError:
        print(f"Il file '{filename_alunni}' non esiste. Assicurati di avere un file con i nomi degli alunni per questa classe.")
        return

    try:
        with open(filename_interrogati, "r") as file:
            alunni_interrogati = file.read().splitlines()
    except FileNotFoundError:
        alunni_interrogati = []

    if quanti < 1 or quanti > len(alunni):
        print(f"Inserisci un numero compreso tra 1 e {len(alunni)}")
        return

    alunni_disponibili = [alunno for alunno in alunni if alunno not in alunni_interrogati]

    if not alunni_disponibili:
        print(f"Hai interrogato tutti gli alunni disponibili nella classe {classe}.")
        return

    alunni_selezionati = random.sample(alunni_disponibili, quanti)

    print(f"Gli alunni interrogati nella classe {classe} sono:")
    for alunno in alunni_selezionati:
        print(alunno)

    with open(filename_interrogati, "a") as file:
        for alunno in alunni_selezionati:
            file.write(alunno + "\n")

classe_da_interrogare = input("Inserisci la classe da interrogare: ")
quantita_da_interrogare = int(input("Quanti alunni vuoi interrogare?"))
interrogare_alunni(classe_da_interrogare, quantita_da_interrogare)
