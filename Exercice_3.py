myTable = [34,2,45,60,10]
taille_myTable = len(myTable)
intermediaire = 0

for i in range (taille_myTable-1):
    for j in range (taille_myTable-1):
        if myTable[j] > myTable[j+1]:
            intermediaire = myTable[j]
            myTable[j] = myTable[j+1]
            myTable[j+1] = intermediaire
print (myTable)