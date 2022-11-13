import socket
from threading import Thread



class SendMessageThread_(Thread):

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            message = input('')
            if message == 'stop':
                client_socket.send(message.encode())
                thread_receiv.stopped()
                self.stopped()
                break
            print(f'My message: \033[32m{message}\033[0m')
            message2 = f'Message from IP:{my_local_ip}: \033[33m{message}\033[0m'
            client_socket.send(message2.encode())

    def stopped(self):
        client_socket.close()

class ReceivMessageThread_(Thread):

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            message_from_server = client_socket.recv(512).decode()
            print(message_from_server)
            if message_from_server == 'stop':
                break
        thread_send.stopped()
        self.stopped()

    def stopped(self):
        client_socket.close()




if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    my_local_ip = s.getsockname()[0]
    s.close()

    local_ip_server = input('Input the local IP of server: ')
    port = 5562

    client_socket = socket.socket()
    client_socket.connect((local_ip_server, port))

    print('\033[32m*** Connected to server... ***\033[0m')
    print('You can write any message.')

    thread_send = SendMessageThread_()
    thread_receiv = ReceivMessageThread_()

    thread_send.start()
    thread_receiv.start()



