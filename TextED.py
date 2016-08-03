from Crypto.Cipher import AES
import base64
import os


def encryption(privateinfo,secret,file_name):
    block_size = 16
    padding = '{'


    pad = lambda s:s + (block_size - len(s) % block_size) * padding

    encodeAES = lambda c,s: base64.b64encode(c.encrypt(pad(s)))

    #secret = os.urandom(block_size)
    #secret = "asdfghjklzxcvbnm" #16 character key
    
    #print 'Encryption key:', secret


    cipher = AES.new(secret)

    encoded = encodeAES(cipher,privateinfo)
    fileN = os.path.splitext(file_name)[0]

    file_nm = fileN + "Enc.txt"

    f = open(file_nm, "w")
    f.write( str(encoded)  )      # str() converts to string
    f.close()


    
    #print "\nEncrypted String:\n",encoded
    

    print "\n\n\n"

def decryption(encryptedstring,key,file_name):
    
    padding = '{'


    

    decodeAES = lambda c,e: c.decrypt(base64.b64decode(e)).rstrip(padding)

    #secret = os.urandom(block_size)
    #key = "asdfghjklzxcvbnm" #16 character key
    
    


    cipher = AES.new(key)

    decoded = decodeAES(cipher,encryptedstring)
    fileN = os.path.splitext(file_name)[0]

    file_nm = fileN + "_to_Original.txt"

    
    f = open(file_nm, "w")
    f.write( str(decoded)  )      # str() converts to string
    f.close()


    
    #print "\nDecrypted String:\n",decoded
    print "\n\n\n"

loop = 1

while(loop):
    
    print "             WELCOME TO THE ENCRYPTOR!!!                 \n"
    choice = int(raw_input('Choose an option.\n      1.Encryption\n      2.Decryption\n      3.Exit\n'))
    if choice == 1:

        
        
        secret = raw_input('Enter a 16 or 32 or 64 char Secret Key to Encrypt: ')
        #privateinfo = raw_input("\nEnter the String to be Encrypted: \n")
        file_name = raw_input("\nEnter the file to be Encrypted: \n")
        #fileN = os.path.splitext(file_name)[0]

        privateinfo = open(file_name, 'r').read()

        encryption(privateinfo,secret,file_name)
        

    elif choice == 2:
        
        
        
        key = raw_input('Enter a 16 or 32 or 64 char Secret Key to Decrypt: ')
        #encryptedstring = raw_input("\nEnter the String to be Decrypted: \n")
        file_name = raw_input("\nEnter the file to be Decrypted: \n")
        #fileN = os.path.splitext(file_name)[0]

        encryptedstring = open(file_name, 'r').read()

        decryption(encryptedstring,key,file_name)
    elif choice == 3:

        loop = 0
        
    else:
        print "Invalid Choice"


