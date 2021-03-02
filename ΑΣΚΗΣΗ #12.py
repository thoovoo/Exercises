#Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο ένα αρχείο ASCII κειμένου και μετατρέπει
#τον κάθε χαρακτήρα του στον “κατοπτρικό” του χαρακτήρα ASCII. Κατοπτρικοί χαρακτήρες είναι αυτοί
#των οποίων το άθροισμα είναι 128. Εμφανίστε το κατοπτρικό κείμενο στο χρήστη με ανάποδη σειρά χαρακτήρων.

def convert (x):
    array=[]
    array2=[]
    
    for i in range(len(x)):
        for j in range(len(x[i])):
            array.append(x[i][j])
    
    for k in range(len(array)):
        num=ord(array[k])
        pal=128-num
        array2.append(pal)

    return array2

def reversal(x):
    
    lista=x[::-1]
    stringlist = "".join([chr(c) for c in lista])  
        
    return stringlist
            
with open ("two_cities_ascii.txt" , "r") as f:
    text = f.readlines()

fstep=convert(text)

sstep=reversal(fstep)


print (sstep)

