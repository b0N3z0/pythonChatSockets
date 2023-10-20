import socket
from _thread import *
def listen(con):
    while True:
        try:
            data = client.recv(1024)  # получаем данные с сервера
            print("Server sent: ", data.decode())
        except:
            con.close()

def send(con):
    while True:
        try:
            message = input("Input a text: ")  # вводим сообщение
            client.send(message.encode())
        except:
            con.close()

client = socket.socket()  # создаем сокет клиента
hostname = socket.gethostname()  # получаем хост локальной машины
port = 12345  # устанавливаем порт сервера
client.connect((hostname, port))  # подключаемся к серверу

start_new_thread(listen, (client,))
start_new_thread(send, (client,))

a = 0
while True:
    a = a