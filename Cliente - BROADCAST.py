import threading
import socket

def main():

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        cliente.connect(('localhost', 7777))
    except:
        return print('\nServidor não iniciado :( \n')

    user = input('Usuário> ')
    print("\n")
    print(user +' conectado(a) ao servidor')

    thread1 = threading.Thread(target = receiveMessages, args = [cliente])
    thread2 = threading.Thread(target = sendMessages, args = [cliente, user])

    thread1.start()
    thread2.start()

def contaVogais(string):
    string = string.lower() 
    vogais = 'aeiou'
    return {i: string.count(i) for i in vogais if i in string}
    print('\n')

def contaConsoantes(string):
    string = string.lower() 
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    return {i: string.count(i) for i in consoantes if i in string}
    print('\n')


def receiveMessages(client):
    while True:
        try:
            mensagem = client.recv(2048).decode('utf-8')
            print(mensagem+'\n')
        except:
            print('\nNão foi possível manter a conexão :( \n')
            client.close()
            break
            
def inverterString(txt):
  return txt[::-1]
  print('\n')

def sendMessages(client, username):
    while True:
        try:
            mensagem = input('\n')
            client.send(f'<{username}> {mensagem}'.encode('utf-8'))
            client.send(f'\n Vogais: {contaVogais(mensagem)}'.encode('utf-8'))
            client.send(f'\n Consoantes: {contaConsoantes(mensagem)}'.encode('utf-8'))
            client.send(f'\n Invertido: {inverterString(mensagem)}'.encode('utf-8'))
            print('\n')
            
        except:
            return


main()