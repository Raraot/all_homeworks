import socket
from threading import Thread


# host = socket.gethostname()
# IP = socket.gethostbyname(host)
# port = 5561
#
# client_socket = socket.socket()
# client_socket.connect((host, port))



#
# def send_message():
#     while True:
#         message = input('')
#         if message == 'stop':
#             client_socket.send(message.encode())
#             break
#         print(f'My message: \033[32m{message}\033[0m')
#         message2 = f'Message from IP:{IP}: \033[33m{message}\033[0m'
#         client_socket.send(message2.encode())
#
#
#     return True
#
#
# def receiv_message():
#     while True:
#         message_from_server = client_socket.recv(512).decode()
#         print(f'{message_from_server}')
#         if message_from_server == 'stop':
#
#             break
#
#     return True

#
# if __name__ == '__main__':
#
#     thread_send = Thread(target=send_message)
#     thread_receiv = Thread(target=receiv_message)
#
#     thread_send.start()
#     thread_receiv.start()

# if (send_message() == True) or (receiv_message() == True):
#     # client_socket.shutdown(socket.SHUT_RDWR)
#     # client_socket.shutdown(socket.SHUT_RDWR)
#     client_socket.close()
#     client_socket.close()
#     thread_send.join()
#     thread_receiv.join()
#     print('Nice exit')



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
            message2 = f'Message from IP:{IP}: \033[33m{message}\033[0m'
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
    host = socket.gethostname()
    IP = socket.gethostbyname(host)
    port = 5562

    client_socket = socket.socket()
    client_socket.connect((host, port))

    thread_send = SendMessageThread_()
    thread_receiv = ReceivMessageThread_()

    thread_send.start()
    thread_receiv.start()



