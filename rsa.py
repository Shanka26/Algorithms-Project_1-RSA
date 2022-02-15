import math
import random



def generatePrime(k):
    
    while True:
        n = random.randint(2, 200)
        if(fermatTest(n,k)):
            return n
    # Fermat's little theorem
            

def fermatTest(n,k):
    for i in range(k):             
        a = random.randint(1, n-1)   
        if pow(a, n - 1, n) != 1:
            return False
                

    return True
                    
         
    

def generateE(m):
   
    while True:
             
        a = random.randint(2, 100)
        if math.gcd(a,m)== 1:
            return a

            
    
def extended_gcd(a=1, b =1):
    if b == 0:
        return (1, 0, a)
    (x, y, d) = extended_gcd(b, a%b)
    return y, x - a//b*y, d
 
   


def fastExpo_recursive(a, p, n):
    if p == 0:
        return 1
    if p%2 == 0:
        t = fastExpo_recursive(a, p//2, n)
        return (t*t)%n
    else:
        t = fastExpo_recursive(a, p//2, n)
        return a *(t**2%n)%n

 
def encrypt(me,e,n):
    
    c=fastExpo_recursive(me,e,n) 
    # c=pow(me,e,n) 
    return c

def encryptString(msg):
    encryptedString=""
    for i in msg:   
        encryptedString+=(chr(encrypt(ord(i),e,n)))
    return encryptedString   
    

def decrypt(me,d,n):
    c=fastExpo_recursive(me,d,n)
    # c=pow(me,d,n) 
    return c

def decryptString(msg):
    decryptedString=""
    for i in msg:   
        de=decrypt(ord(i),d,n)
        decryptedString+=chr(de)
    return decryptedString 



# test valuesss
# p=7
# q=17
# e=5
# d=77


p=generatePrime(1000)
q=generatePrime(1000)
n=p*q
m=(p-1)*(q-1)
e=generateE(m)

d,a,b=extended_gcd(e,m)


print(decryptString(encryptString("It works sometimes")))

