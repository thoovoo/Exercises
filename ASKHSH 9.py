# Exercise 9
# Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο ένα αρχείο ASCII κειμένου και μετατρέπει τον κάθε χαρακτήρα 
# στον αντίστοιχο αριθμό ASCII και κρατάει τους μονούς. Εμφανίστε τα στατιστικά εμφάνισης του κάθε γράμματος με “μπάρες” 
# χρησιμοποιώντας το χαρακτήρα *, όπου κάθε * αντιστοιχεί σε 1%. Η στρογγυλοποίηση θα γίνει προς τα πάνω.

def convert (x):
    array=[]
    array2=[]
    
    for i in range(len(x)):
        for j in range(len(x[i])):
            array.append(x[i][j])
    array.sort()
    
    for k in range(len(array)):
        num=ord(array[k])
        if num % 2 !=0:
            array2.append(num)

    return array2


def counting (w):
    x = []
    y = []
    z=0
    for i in range(len(w)):                     
        if nums[i] not in x:          
            a = 0                         
            b = w.count(w[i])
            a = b  
            x.append(nums[i])
            y.append(a)
            z+=a

    return x,y,z
#with open ("two_cities_ascii.txt" , "r") as f:
#    text = f.readlines()
text=("It was the best of times, it was the worst of times, it was the age of")

nums=convert (text)
once,found,suma = counting(nums)
 
pos=[]
for i in range(len(found)):
    x = (found[i]*100)/suma
    pos.append(x)
    
for j in range(len(pos)): 
    if pos[j] == int(pos[j]):
        pos[j] = pos[j]
    elif pos[j] < 1:
        pos[j] = 1
    elif pos[j]%int(pos[j]) <= 0.5 :
        pos[j] = int(pos[j]) + 1
    else:
        pos[j] = round(pos[j])  


small = ['a','s','d','f','g','h','j','k','l','q','w','e','r','t','y','u','i','o','p','z','x','c','v','b','n','m']
n=[ord(cs) for cs in small]


caps = ['A','S','D','F','G','H','J','K','L','Q','W','E','R','T','Y','U','I','O','P','Z','X','C','V','B','N','M']
d=[ord(cc) for cc in caps]


ols = []
olc = []

for s in range(len(n)):
    if n[s]%2 != 0:
        ols.append(n[s])

for c in range (len(d)):
    if d[c]%2 != 0:
        olc.append(d[c])



for m in range(len(pos)):
    if chr(once[m]) in ols or chr(once[m]) in olc:
        print ((str(once[m])+ ' - ' + chr(once[m]) + ": " + "*"*pos[m] + ' ' + str(pos[m]) + '%'))

