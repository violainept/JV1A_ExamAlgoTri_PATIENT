myTable = [34,2,45,60,10]
taille_myTable = len(myTable)
intermediaire = 0

for i in range (taille_myTable-1):
    if myTable[i] > myTable[i+1]:
        intermediaire = myTable[i]
        myTable[i] = myTable[i+1]
        myTable[i+1] = intermediaire
print (myTable)