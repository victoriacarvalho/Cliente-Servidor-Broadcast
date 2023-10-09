import threading
import socket

clients = []

print("\n Servidor conectado :)  \n")
print(" Inicie os clientes   \n")

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(('localhost', 7777))
        server.listen()
    except:
        return print('\nServidor não conectado :( \n')

    while True:
        client, addr = server.accept()
        clients.append(client)

        thread = threading.Thread(target = messagesTreatment, args = [client])
        thread.start()

def messagesTreatment(client):
    while True:
        try:
            mensagem = client.recv(2048)
            broadcast(mensagem, client)
        except:
            deleteClient(client)
            break

def broadcast(mensagem, client):
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(mensagem)
            except:
                deleteClient(clientItem)

def deleteClient(client):
    clients.remove(client)

main()
