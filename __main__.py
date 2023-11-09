
def main():
    print("hello world")
    
message = "Top Secret Message"
salt = "20" #generate with hash?
   
def encrypt(message, salt):
    #convert message to binary
    msg =  message + salt
    binary = toBinary(msg)
    decimalText = binaryToDecimal(binary)
    print(binary, decimalText)
      
def decrypt(message, salt):
        decryptedMessage = salt.decode()() + message.decode()
        print(decryptedMessage)
        
        
def toBinary(inputValue):
    returnValue =  ' '.join(format(ord(x), 'b') for x in inputValue)
    return returnValue

def binaryToDecimal(binary):
 
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal
     
if __name__ == "__main__":  
    encrypt(message, salt)
    #decrypt(message, salt)
    
    

    
 