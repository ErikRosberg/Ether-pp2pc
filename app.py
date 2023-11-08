connection_IP = input("IP to connect to ")
local_Ip = "192.168.1.1"

if connection_IP:
    result = checkConnection(connection_IP)
    if result == 200:
        if connectionAccepted == 1:
            print("Connection OK")
        else if connectionAccepted == 0:
            print("Connection Refused")
        else:
            print("Connection Timedout")

    else:
        print("failed to establish connection to {} try again".format(connection_IP))

msg = str(input("Write Message ... msg"))

print(msg)
