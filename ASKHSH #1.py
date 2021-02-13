# Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει την διάσταση ενός τετραγώνου και θα φτιάχνει μέσα από λίστες τον αντίστοιχο πίνακα.
# Στην συνέχεια θα βρίσκει το πλήθος των θέσεων και θα γεμίζει στην τύχη τις μισές με μονάδες (στρογγυλοποίηση προς τα πάνω).
# Σκοπός είναι να μετρήσετε πόσες τετράδες από μονάδες υπάρχουν οριζόντια, κάθετα, και διαγώνια.
# Το πρόγραμμα επαναλαμβάνεται 100 φορές (για την ίδια διάσταση) και επιστρέφει τον μέσο όρο των τετράδων.



import numpy as np

def createMatrix(x): # ΔΗΜΙΟΥΡΓΙΑ ΠΙΝΑΚΑ
    if (s**2)%2!=0: #ΥΠΟΛΟΓΙΣΜΟΣ ΑΣΣΩΝ
        aces=int(((s**2)+1)/2)
    else:
        aces=int((s**2)/2)
    zeros=int((s**2)-aces) #ΥΠΟΛΟΓΙΣΜΟΣ ΜΗΔΕΝΙΚΩΝ
    a=[]
    for i in range (aces):
        a.append(1)
    for j in range (zeros):
        a.append (0)
    np.random.shuffle(a) #ΑΝΑΚΑΤΕΜΑ ΛΙΣΤΑΣ
    b=[]
    b = np.reshape(a,(s,s,)) #ΤΕΛΙΚΗ ΜΟΡΦΟΠΟΙΗΣΗ ΠΙΝΑΚΑ
    matrix=[]
    factor = 0
    for k in range(0, s):
        row = []
        for l in range(factor * s, (factor + 1) * s):
            row.append(a.pop(0))
        factor += 1
        matrix.append(row)
        k += 1
    return b,matrix

def countInCols(matrix):  #ΑΝΑΖΗΤΗΣΗ ΚΑΘΕΤΑ. ΜΕΧΡΙ ΕΔΩ ΟΚ
    cMatching=0
    counter=0
    while counter<len(matrix):
        columnForSearch = [row[counter] for row in matrix]
        for n in range (len(matrix)-3):
            if columnForSearch[n]==1 and columnForSearch[n+1]==1 and columnForSearch[n+2]==1 and columnForSearch[n+3]==1:
                cMatching+=1
        counter+=1
    return cMatching

def countInRows(matrix): #ΑΝΑΖΗΤΗΣΗ ΟΡΙΖΟΝΤΙΑ. ΜΕΧΡΙ ΕΔΩ ΟΚ
    rMatching=0
    counter=0 
    while counter<=len(matrix):
        for r in range(len (matrix)-1):            
            rowForSearch= matrix[r][:]
            for h in range (len(rowForSearch)-3):
                if rowForSearch[h]==1 and rowForSearch[h+1]==1 and rowForSearch[h+2]==1 and rowForSearch[h+3]==1:
                    rMatching=+1
            counter+=1
    return rMatching

def countInDiagonals(matrix):  #ΑΝΑΖΗΤΗΣΗ ΔΙΑΓΩΝΙΑ. ΜΕΧΡΙ ΕΔΩ ΟΚ
    n=len(matrix)
    diagonals = []
    xMatching=0
    for p in range(2*n-1):
        diagonals.append([matrix[p-q][q] for q in range(max(0, p - n + 1), min(p, n - 1) + 1)])
        diagonals.append([matrix[n-p+q-1][q] for q in range(max(0, p - n + 1), min(p, n - 1) + 1)])
    for i in diagonals:
        if len(i)>=4:
            for j in range (len(i)-3):
                if i[j]==1 and i[j+1]==1 and i[j+2]==1 and i[j+3]==1:
                    xMatching+=1
    return xMatching


        
s=int(input("Δηλώστε μέγεθος πλευράς τετραγώνου: "))

board,board_r=createMatrix(s)

totalV=0
for v in range(100):
    vertical=countInCols(board)
    totalV+=vertical
avgV=int(totalV*0.01)

totalH=0
for h in range(100):
    horizontal=countInRows(board_r)
    totalH+=horizontal
avgH=int(totalH*0.01)

totalX=0
for d in range (100):
    xdiagonals=countInDiagonals(board)
    totalX+=xdiagonals
avgX=int(totalX*0.01)

print ("Σε τετράγωνο πλευράς", s ,"ψηφίων, σε 100 επαναλήψεις εμφανίζονται κατα μέσο όρο", avgV ,"τετράδες κάθετα,", avgH ,"τετράδες οριζόντια και", avgX ,"τετράδες διαγώνια.") 
