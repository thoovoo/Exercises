#Γράψτε ένα κώδικα σε Python ο οποίος ελέγχει αν ο ν όρος της ακολουθίας Fibonacci είναι πρώτος ή όχι.
#Για να απαντήσετε αν ένας αριθμός p είναι πρώτος θα πρέπει για 20 τυχαίες επιλογές του a
#να ισχύει ότι a^p=a mod p.
#Ο κώδικάς σας παίρνει τον όρο της ακολουθίας Fibonacci από το χρήστη.

import random
from random import randint


def searchFibonacci(n):
    a = 0
    b = 1
    c = 1
    for i in range(2,n):
        c = a + b
        a = b
        b = c
    return (c)

def testForPrimal(p):
    used=[]
    isprimal=True
    count=0
    multi=0
    divisor=0
    value = randint(0, p)
    left=0
    right=value % p    
    while isprimal==True:
        while count<20:
            if value not in used:
                multi=value
                times=1
                a_mod_p=value % p
                while times<p:
                    multi*=value
                    times+=1            
                used.append(value)
                count+=1
                while divisor<multi:
                    divisor+=p
                left=multi - divisor
                if left==right:
                    isprimal=True
                else:
                    isprimal=False
                    return isprimal
                value = randint(0, p)
            else:
                value = randint(0, p)
    return isprimal


def testForPrimal2(p):
    isprimal=True
    left=multi % p
    right=value % p
    while isprimal==True:
        for i in p:
            if value not in used:
                multi=0
                times=1
                a_mod_p=value % p
                while times<p:
                    multi*=value
                    times+=1
                if left==right:
                    isprimal=True
                else:
                    isprimal=False
    return isprimal
    

fn=int(input("Δώσατε όρο της ακολουθίας Φιμπονάτσι προς αναζήτηση; "))

num=(searchFibonacci(fn))

if num>20:
    cp=(testForPrimal(num))
else:
    cp=(testForPrimal2(num))
    
if cp==True:
    print ("Ο αριθμός", num ,"(No", fn , "όρος της ακολουθίας Φιμπονάτσι), είναι πρώτος αριθμός")
else:
    print ("Ο αριθμός", num ,"(No", fn , "όρος της ακολουθίας Φιμπονάτσι), δεν είναι πρώτος αριθμός")
