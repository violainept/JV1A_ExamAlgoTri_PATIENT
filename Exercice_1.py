myTable = [5,24,35,40]
valeur_A = 0
valeur_B = 2
intermediaire = 0

intermediaire = myTable[valeur_A]
myTable[valeur_A] = myTable[valeur_B]
myTable[valeur_B] = intermediaire

print (myTable)