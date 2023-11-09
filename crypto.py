import hashlib

message = "hello World"
salt = 20


def hashInput(message, salt):
    messageInt = int(message)
    print(messageInt, "first")
    hex(messageInt)
    print(messageInt, "second")


    bin(messageInt) # Result: '0b1111100010110000001101011111'
    int(str(messageInt)[2:])
    
    #convert string to hexadecimals/int or binary?
    #hash it with a math calc
    #convert the int/hexadesimal to a string
    #return the new string
    
    messageInt = int(salt, 0)
    print(messageInt, "third")

    hashedMessage = str(messageInt)
    return hashedMessage
    
    
def presetHash(message, salt):
    msgStr = str(message)
    saltint = int(salt)
    h = hashlib.new('sha256')
    h.update(b, msgStr)
    h.hexdigest(saltint)
    #hash more? how to use salt?
    hashedMessage = h.hexdigest(saltint)
    
    
def presetHash2(message, salt):
    h = hashlib.new('sha256')
    h.update(salt.encode() + message.encode())
    hashedMessage = h.hexdigest()
    return hashedMessage
