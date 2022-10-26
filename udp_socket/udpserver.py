from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("Ascolto nella socket per la ricezione di pacchetti da client(s)")
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    print("Ricevuto: ")
    print(message)
    print("Convertito in maiuscolo")
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
