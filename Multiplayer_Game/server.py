import socket
from _thread import *

server = "192.168.29.48"  # Local IP Address
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Type of connection IPV4

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server started")


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


pos = [(0, 0), (100, 100)]


def threaded_client(conn, player):
    # pass
    # conn.send(str.encode("Connected"))
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            # reply = data.decode("utf-8")
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                # print("Received: ", reply)
                print("Received: ", data)
                print("Sending: ", reply)

            # conn.sendall(str.encode(reply))
            conn.sendall(str.encode(make_pos(reply)))
        except:
            break

    print("Lost connection")
    conn.close()


currentPlayer = 0
while True:
    conn, addr = s.accept()  # Accept connection
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))  # dont wait for function to complete
    currentPlayer += 1
