#print(Citește  două mase pozitive, în kg. Afișează masa totală în kg și în grame)
m1 = float(input("Introduceti prima masă (în kg): "))
m2 = float(input("Introduceti a doua masă (în kg): "))
mt = m1 + m2
print(f"Masa totală este: {mt:.2f} kg")
print(f"Masa totală este: {mt * 1000:.2f} g")