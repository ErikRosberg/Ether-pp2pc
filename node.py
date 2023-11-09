import socket 
import sys 


def listener(): 		 
    # next create a socket object 
    s = socket.socket()		 
    print ("Socket successfully created")

    # reserve a port on your computer in our 
    # case it is 12345 but it can be anything 
    port = 12345			

    # Next bind to the port 
    # we have not typed any ip in the ip field 
    # instead we have inputted an empty string 
    # this makes the server listen to requests 
    # coming from other computers on the network 
    s.bind(('', port))		 
    print ("socket binded to %s" %(port)) 

    # put the socket into listening mode 
    s.listen(5)	 
    print ("socket is listening")		 

    # a forever loop until we interrupt it or 
    # an error occurs 
    while True: 

        # Establish connection with client. 
        c, addr = s.accept()	 
        print ('Got connection from', addr )

        # send a thank you message to the client. encoding to send byte type. 
        c.send('Thank you for connecting'.encode()) 

        # Close the connection with the client 
        c.close()

        # Breaking once connection closed
        break

def client():

    # Create a socket object 
    s = socket.socket()		 

    # Define the port on which you want to connect 
    port = 12345			

    # connect to the server on local computer 
    s.connect(('127.0.0.1', port)) 

    # receive data from the server and decoding to get the string.
    print (s.recv(1024).decode())
    # close the connection 
    s.close()	 
	
	