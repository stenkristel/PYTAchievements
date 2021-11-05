def bereken_maandkosten():
    benzinekosten = km_per_maand * 0.2 * 1.45
    maandkosten = benzinekosten + 23
    return maandkosten

print ("Hoeveel kilometer per maand rij jij op je scooter")
km_per_maand = input("Kilometer: ")
km_per_maand = float(km_per_maand)


print(bereken_maandkosten())