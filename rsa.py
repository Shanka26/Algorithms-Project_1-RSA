from email import message_from_file
import math
import random
from unicodedata import decimal



def generatePrime(k):
    # Continue to generate random numbers and test if they are pseudo prime
    while True:
        n = random.randint(1000000, 100000000)
        if(fermatTest(n,k)):
            return n
    
            

def fermatTest(n,k):
    # Fermat's little theorem
    for i in range(k):             
        a = random.randint(1, n-1)   
        if pow(a, n - 1, n) != 1:
            return False
    return True
                    
 
    

def generateE(m):
   
    while True:
    
        a = random.randint(1000000, 100000000)
        if math.gcd(a,m) == 1:
            return a
       
            
    
def extended_gcd(a=1, b =1):
    if b == 0:
        return (1, 0, a)
    (x, y, z) = extended_gcd(b, a%b)
    return y, x - a//b*y, z
 
def generatePrivateKey(e,m):
    (z,a,b)=extended_gcd(e,m)
    if z < 0:
        z = m + z
    return z
   


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
    encryptedString=[]
    for i in msg:   
        encryptedString.append((encrypt(ord(i),e,n)))
    return encryptedString   

def encryptWholeString(msg):

    #Break string into 4-char blocks and place in list
        #Pad message to multiple of 5 chars
    msgLen = len(msg)
    if msgLen % 4 != 0:
        msg = msg + '_' * (4 - (msgLen % 4))
    msgLen = len(msg)

        #Slice blocks of message into list
    msgBlocks = []
    for i in range(msgLen//4):
        msgBlocks.append(msg[ 4*i : 4*i + 4])

    #Convert each block to ints and encrypt
    for i in range(len(msgBlocks)):
        msgInt = '1' #Leading 1 protects leading 0s from being truncated, maintaining parable triplets
        for j in msgBlocks[i]:
            msgInt += '%03d' % ord(j)  #outputs the 3 digit ascii encoding of each character
        msgBlocks[i] = int(msgInt)

    #Encrypt msgBlocks
    for i in range(len(msgBlocks)):
        msgBlocks[i] = encrypt( msgBlocks[i], e, n)

    return msgBlocks   
    
def decrypt(me,d,n):
    c=fastExpo_recursive(me,d,n)
    # c=pow(me,d,n) 
    return c

def decryptString(msg):
    decryptedString=""
    for i in msg:   
        de=decrypt(i,d,n)
        decryptedString+=chr(de)
    return decryptedString 

def decryptWholeString(msgBlocks):
    #Decrypt each i in msgBlocks
    for i in range(len(msgBlocks)):
        print(msgBlocks[i])
        msgBlocks[i] = decrypt(msgBlocks[i], d, n)
        print(msgBlocks[i])
    #Parse characters back out of msgBlocks
    msg = ''
    for i in msgBlocks:
        for j in range(4):
            msgInt = str(i)[ 3*j + 1 : 3*j + 4] #indexes past the leading '1'
            msgInt = int(msgInt.lstrip('0')) #strips leading 0s from triples
            msg += chr(msgInt)
    msg = msg.rstrip('_')

    return msg


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
d=generatePrivateKey(e,m)
print("p"+str(p)+":q"+str(q)+" - e"+str(e))
print(decryptString(encryptString("It works perfectly")))

msg = 'Does this work for arbitrarily long strings...? What about funny characters like @%$#'
encMsg = encryptWholeString(msg)
print(encMsg)
decryptWholeString(encMsg)
