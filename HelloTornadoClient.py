import socket
import sys
#expCount 

#------------------

def CheckPort(host, port):
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((host, port))
    except socket.error as msg:
        print(msg)
        print("Port ", port, " of host ", host, " is closed or something")
        pass
    else:
        s.close
        print(host + ": "  + str(port) + " порт активен ")
        return 1
    return 0
    
    

