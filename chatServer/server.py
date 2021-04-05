#Jesus Ugarte
# University of Central Florida
# Chat Server

import socket
import threading 

host = '127.0.0.1' #localhost
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients =[]
nicknames =[]

def broadcast(message):

    #Broadcasting messge to all clients
    for client in clients:
        client.send(message)

def kick_user(name):
    if name is nicknames:
        name_index = nickname.index(name)
        client_to_kick = clients[name_index]
        clients.remove(client_to_kick)
        client_to_kick.send('You wwere kicked by admin!'.encode('ascii'))
        client_to_kick.close()
        nicknames.remove(name)
        broadcast(f'{name} was kicked by an admin'.encode('ascii'))


def command_handle(message):

    if msg.decode('ascii').startswith('KICK'):
        if nicknames[clients.index(client)] == 'admin':
            name_to_kick = msg.decode('ascii')[5:]
            kick_user(name_to_kick)
        else: #Making sure server is not exploited
            client.send('Command was refused!'.encode('ascii'))
    elif msg.decode('ascii').startswith('BAN'):
        if nicknames[clients.index(client)] == 'admin':
            name_to_ban = msg.decode('ascii'[4:])
            kick_user(name_to_kick)
            with open('bans.txt', 'a') as f:
                f.write(f'{name_to_ban}\n')
            print(f'{name_to_ban} was banned!')
        else:#Making sure server is not exploited
            client.send('Command was refused!'.encode('ascii'))
    else:
        broadcast(message)

def handle(client):

    #Handling disconnection username exceptions
    while True:
        try:
            msg = message = client.recv(1024)

            #handle command instructions 
            command_handle(message)

            broadcast(message)

        except:
            if client in clients:
                index = xlients.indeex(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f'{nickname} left the chat!'.encode('ascii'))
                nicknames.remove(nickname)
                break

def receive():
    while True:
        #Accept the new connection
        client, address = server.accept()
        print(f"Conncected with {str(address)}")

        clients.send('NICK'.encode('ascii'))
        nickename = client.recv(1024).decode('ascii')

        with open('bans.txt', 'r') as f:
            bans = f.readlines()

        if nickname+'\n' in bans:
            client.send('BAN'.encode('ascii'))
            client.close()
            continue

        #Checking for admin priviledge
        if nickname =='admin':
            client.send('PASS'.encode('ascii'))
            password = client.recv(1024).decode('ascii')

            #NOT SECURE WAY TO CHECK FOR PASSWORD
            if password != 'adminpass':
                client.send('REFUSE'.encode('ascii'))
                client.close()
                continue

        nicknames.append(nickname)
        
        #Broadcasting all the membes that a member has joined 
        print(f"Nickname of the client is {nickname}!")
        broadcast(f'{nickname} joined the chat!'.encode('ascii'))
        client.send("Connected to the server!".encode('ascii'))
        
        #Start threading using handle function
        thread = threading.Thread(target=handle , args = (client, ))
        thread.start()

print("Server is listening...")
receive()