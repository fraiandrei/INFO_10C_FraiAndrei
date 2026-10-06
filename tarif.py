Putere=int(input('Dati puterea(w):'))
Timp=int(input('Dati timpul(h):'))
Energie=Putere*Timp/1000
print(f'spre achitare {Energie:.2f}kwh')
Tarif=float(input('Dati tariful actual:'))
Cost=Energie*Tarif
print(f'spre achiare{Cost:.2f}')