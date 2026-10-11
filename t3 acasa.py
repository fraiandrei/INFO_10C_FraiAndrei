#print(Citește distanța în km și consumul în L/100 km.Calculează combustibilul necesar. Datele de intrare sunt pozitive.)
d = float(input("Introduceti distanța (în km): "))
c = float(input("Introduceti consumul (în L/100 km): "))
combustibil = (d * c) / 100
print(f"Combustibilul necesar este: {combustibil:.2f} L")