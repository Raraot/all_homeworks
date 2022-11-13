import socket
from threading import Thread


class SendMessageThread(Thread):

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            message = input('')
            if message == 'stop':
                conn.send(message.encode())
                thread_receiv_serv.stopped()
                self.stopped()
                break
            print(f'My message: \033[32m{message}\033[0m')
            message2 = f'Message from IP:{local_ip}: \033[33m{message}\033[0m'
            conn.send(message2.encode())

    def stopped(self):
        conn.close()

class ReceivMessageThread(Thread):

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            message_from_client = conn.recv(512).decode()
            print(message_from_client)
            if message_from_client == 'stop':
                break
        thread_send_serv.stopped()
        self.stopped()

    def stopped(self):
        conn.close()




if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    s.close()

    port = 5562
    print(f'My local IP: \033[35m{local_ip}\033[0m\n'
          f'you must to input this IP in client app')
    server_socket = socket.socket()
    server_socket.bind((local_ip, port))
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print('\033[32m   *** Connected... ***\033[0m')
    print('You can write any message.')

    thread_send_serv = SendMessageThread()
    thread_receiv_serv = ReceivMessageThread()

    thread_send_serv.start()
    thread_receiv_serv.start()

