from enum import Enum
class Stare(Enum):
    NOU = "nou"
    LUCRU = 'lucru'
    GATA = "gata"
s = Stare("gata")
print(s.name, s.value)

