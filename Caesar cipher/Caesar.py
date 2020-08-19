from string import ascii_lowercase #imports strings of aphabet


def return_alpha_index(a):
    """ returns the index of an alphabet """
    alphabets = ascii_lowercase
    for i,j in enumerate(alphabets):
       if j == a:
           return(i)
    return(a)

def return_index_alpha(n):
    """ returns an alphabet given the index"""
    alphabets = ascii_lowercase
    for i,j in enumerate(alphabets):
       if i == n:
           return(j)
    return(n)


def encryption(text,key=13):
    encryption,result = [],[]
    #get the index of the alphabets in text and add the key to them
    for i in text:
        try:
            encryption.append(return_alpha_index(i)+key)
        except:
            encryption.append(return_alpha_index(i))
    #check if a number value is greater than six then subtracts 26 from it 
    for i in encryption:
        try:
            if i >= 26:
                result.append(i-26)
            else:
                result.append(i)
        except:
            result.append(i)
    #get the new number values which is our cipher text
    encryption = "".join([return_index_alpha(n) for n in result])
    return(encryption)


def decryption(text,key=13):
    encryption,result = [],[]
    #get the index of the alphabets in text and subtract the key from them
    for i in text:
        try:
            encryption.append(return_alpha_index(i)-key)
        except:
            encryption.append(return_alpha_index(i))
    #check if a number value is less than 0 then add 26 to it 
    for i in encryption:
        try:
            if i < 0:
                result.append(i+26)
            else:
                result.append(i)
        except:
            result.append(i)
    #get the new number values which is our cipher text
    encryption = "".join([return_index_alpha(n) for n in result])
    return(encryption)


key = 13
text = "Hello this is an encrypted message"
encrypt = encryption(text,key=key)
decrypt = decryption(encrypt,key=key)


print("Text :%s"%text)
print("encrypt :%s"%encrypt)
print("decryption :%s"%decrypt)
    
    
        
