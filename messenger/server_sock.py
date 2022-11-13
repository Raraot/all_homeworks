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
            message2 = f'Message from IP:{IP}: \033[33m{message}\033[0m'
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
    host = socket.gethostname()
    IP = socket.gethostbyname(host)
    port = 5562

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, address = server_socket.accept()

    thread_send_serv = SendMessageThread()
    thread_receiv_serv = ReceivMessageThread()

    thread_send_serv.start()
    thread_receiv_serv.start()

