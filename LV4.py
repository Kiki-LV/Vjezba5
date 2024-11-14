n = int(input("Koliko brojeva želite unjeti za provjeru parnosti? "))

parni_brojevi = 0
neparni_brojevi = 0

for i in range(n):
    broj = int(input(f"Unesite broj {i+1}"))

    if broj % 2 == 0:
        print(f"Broj {broj} je paran.")
        parni_brojevi += 1
    else:
        print(f"Broj {broj} je neparan.")
        neparni_brojevi += 1


print("\nUkupno parnih brojeva:", parni_brojevi)
print("Ukupno neparnih brojeva:", neparni_brojevi)