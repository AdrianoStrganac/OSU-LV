"""
ZADATAK 1.

def total_euro(radni_sat, satnica):
    zaradjeno = radni_sat * satnica
    print("Ukupno", zaradjeno)


radni_sati = float(input("Radni sati: "))
satnica = float(input("eura/h: "))

zarada = radni_sati * satnica
total_euro(radni_sati, satnica)
"""
"""

ZADATAK 2. 

try:
    ocjena = float(input("Unesite ocjenu: "))

    if 0.0 <= ocjena <= 1.0:
        kategorije = {
            "A": (0.9, 1.0), 
            "B": (0.8, 0.9),
            "C": (0.7, 0.8),
            "D": (0.6, 0.7),
            "F": (0.0, 0.6)}
        
        for kategorija, (dg, gg) in kategorije.items():
            if dg <= ocjena <= gg:
                print(kategorija)
                break
    else:
        print("Greska: ocjena mora biti izmedju 0.0 i 1.0")

except ValueError:
    print("Error: Unos nije broj")

"""
"""
ZADATAK 3.

print("Ako zelite prekinut unos brojeva upisite: Done")
broj = 2
numbersList = []
while broj > 1:
    unos = input("Unesite broj: ")
    if unos.lower() == "Done":
        break

    try:
        novi_broj = float(unos)
        numbersList.append(novi_broj)
    except ValueError:
        print ("Error: unos nije broj, pokusajte ponovno")

if(numbersList):
    print(numbersList)
    print(numbersList.sort)
    print("Broj clanova liste",len(numbersList))
    srednja = sum(numbersList) / len(numbersList)
    maks = max(numbersList)
    min = min(numbersList)
    print(srednja, maks, min)
else:
    print("Lista je prazna!")
"""

"""
ZADATAK 4.


from collections import Counter

with open('song.txt', 'r') as file:
    tekst = file.read().lower()
rijeci = tekst.split()

brojac = Counter(rijeci)

print(f"Broj rijeci koje se pojavljuju samo jednom: {sum(1 for count in brojac.values() if count == 1)}")
print("Rijeci koje se pojavljuju samo jednom:")
for rijec, broj in brojac.items():
    if broj == 1:
        print(rijec)

"""
"""
ZADATAK 5.
ham_rijeci = []
spam_rijeci = []
spam_s_usklicnikom = 0

with open('SMSSpamCollection.txt', 'r', encoding='utf-8') as file:
for linija in file:
vrsta, poruka = linija.split('\t', 1)
rijeci = poruka.split()

if vrsta == 'ham':
ham_rijeci.append(len(rijeci))
elif vrsta == 'spam':
spam_rijeci.append(len(rijeci))
if poruka.strip().endswith('!'):
spam_s_usklicnikom += 1

print(f"Prosjecan broj rijeci u ham porukama: {sum(ham_rijeci) / len(ham_rijeci):.2f}")
print(f"Prosjecan broj rijeci u spam porukama: {sum(spam_rijeci) / len(spam_rijeci):.2f}")
print(f"Broj spam poruka koje zavrsavaju usklicnikom: {spam_s_usklicnikom}")

"""