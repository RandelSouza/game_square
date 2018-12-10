from socket import *

class Cliente(object):
    def __init__(self):
        self.serverName = "localhost"
        self.serverPort = 8889
        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        self.clientSocket.connect((self.serverName, self.serverPort))

    def send_message(self, string):
        self.clientSocket.send(string)

    def recieve_message(self):
        return self.clientSocket.recv(1024)
