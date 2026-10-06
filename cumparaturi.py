Pret_initial=float(input('Pretul?:'))
Reducere=int(input('Reducere %:'))
Pret_final=Pret_initial*(Reducere/Pret_initial)
print(f'spre achitare{Pret_final:.2f}lei')
Economie=Pret_final-Pret_initial
print(f'Economie{Economie:.2f}lei')
