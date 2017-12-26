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
            print 'já chegou aqui'
            data = pickle.loads(conn.recv(512))
            print data
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
    print len(List_connection), ' tamanho da lista'
    print "Adicionou conexão"

    conn.send(pickle.dumps(connected))
    print "enviando ", connected
    print "Rodou a thread"

    conn.send(pickle.dumps(connected))
    print "enviando ", connected
    print "Rodou a thread"

    start_new_thread(clientthread, (conn, List_connection))
    connected += 2