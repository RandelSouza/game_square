# -*- coding:UTF-8 -*-
import socket, setup
import pickle
import sys
from thread import *
import traceback

HOST = ''
PORT = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(None)

print "Criou o socket servidor"

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

s.listen(2)

print "Esperando duas conexões"

def clientthread(conn, List_connection):

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

List_connection = []
connected = -1

while True:
    conn, addr = s.accept()
    print "Aceitou a conexão"

    List_connection.append(conn)
    print "Adicionou a conexão"

    conn.send(pickle.dumps(connected))
    print "enviando ", connected

    start_new_thread(clientthread, (conn, List_connection))
    print "Rodou a thread"
    connected += 2
