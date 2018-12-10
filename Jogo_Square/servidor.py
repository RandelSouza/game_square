# -*- coding:UTF-8 -*-
# Classe Servidora
# Estruturar em OO

import socket, setup
import pickle
import sys
from thread import *
import traceback

class servidor(object):
    def __init__(self):
        self.HOST = ''
        self.PORT = 8889
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.settimeout(None)
        self.s.bind((self.HOST, self.PORT))
        self.s.listen(2)
        self.List_connection = []
        self.connected = -1

    def clientthread(self, conn, List_connection):
        try:
            while True:
                data = pickle.loads(conn.recv(512))

                if not data:
                    break
                for i in List_connection:
                    if i != conn:
                        i.send(pickle.dumps(data))
        except Exception:
            print traceback.format_exc(), " error"

server = servidor()

while True:
    conn, addr = server.s.accept()
    print "Aceitou a conexão"

    server.List_connection.append(conn)
    print "Adicionou a conexão"

    conn.send(pickle.dumps(server.connected))
    print "enviando ", server.connected

    start_new_thread(server.clientthread, (conn, server.List_connection))
    print "Rodou a thread"
    server.connected += 2
