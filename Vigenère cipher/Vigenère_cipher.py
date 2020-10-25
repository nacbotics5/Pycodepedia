from random import choice
from string import printable,ascii_lowercase


def return_alpha_index(a):
    """ returns the index of an alphabet """
    alphabets = printable
    #alphabets = ascii_lowercase
    for i,j in enumerate(alphabets):
       if j == a:
           return(i)
    return(a)

def return_index_alpha(n):
    """ returns an alphabet given the index"""
    alphabets = printable
    #alphabets = ascii_lowercase
    for i,j in enumerate(alphabets):
       if i == n:
           return(j)
    return(n)



    
def Encrypt(text,key):
    key = [return_alpha_index(x) for x in key]
    text = [return_alpha_index(x) for x in text]
    
    lst = []

    id = 0
    for i in text:
        if i == " ":
            lst.append(" ")
        else:
            result = i+key[id]
            if result >= 100:#26
                lst.append(result-100)#26
            else:
                lst.append(result)
            
            id += 1
            if id == len(key):
                id = 0
    return("".join([return_index_alpha(i) for i in lst]))

def Decrypt(text,key):
    key = [return_alpha_index(x) for x in key]
    text = [return_alpha_index(x) for x in text]
    
    lst = []

    id = 0
    for i in text:
        if i == " ":
            lst.append(" ")
        else:
            result = i-key[id]
            if result < 0:
                lst.append(result+100)#26
            else:
                lst.append(result)
            
            id += 1
            if id == len(key):
                id = 0
    return("".join([return_index_alpha(i) for i in lst]))


text = "common sense is not so common truth can only be found in the code talk is cheap show me the code"

key = "pycodepedia"
	
encryption = Encrypt(text,key)
decryption = Decrypt(encryption,key)


print(f"TEXT :: {text}")
print(f"KEY  :: {key}")
print(f"ENCRYPTION :: {encryption}")     
print(f"DECRYPTION :: {decryption}")

  
