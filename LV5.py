def provjera_broja(broj):
    if 10 <= broj <= 100:
        return f"Broj {broj} je unutra raspona."
    else:
        return f"Broj {broj} je izvan raspona."

if __name__ == "__main__":
    try:
        uneseni_broj = int(input("Unesite broj:"))
        print(provjera_broja(uneseni_broj))
    except ValueError:
        print("unesena vrijednost nije broj.")