import socket
import md5
import threading

def encode_password(password):
    return md5.new(password).digest()

class User:
    users = {
            "user1": encode_password("abc123"),
            "user2": encode_password("password_123"),
            "user3": encode_password("password_abc")
        }

    @staticmethod
    def check_login(username, password):
        return (username in User.users and User.users[username] == encode_password(password))

class MyServer:
    def __init__(self, host = 'localhost', port = 5000):
        self.host = host
        self.port = port
        self.backlog = 5
        self.buf_size = 1024

        self.users = {
            "user1": encode_password("abc123"),
            "user2": encode_password("password_123"),
            "user3": encode_password("password_abc")
        }

        self.clients = []

        print "Starting the server..."

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(self.backlog)

        print "Server is running on %s:%s" % (self.host, self.port)

    def run(self):
        try:
            while True:
                client_socket, address = self.socket.accept()

                client = MyClient(client_socket, address)
                client.start()
                self.clients.append(client)
        finally:
            print "Shutting down..."

            # on exit
            for c in self.clients:
                c.join()

            self.socket.close()

            print "Bye!"

class MyClient(threading.Thread):
    def __init__(self, socket, address):
        threading.Thread.__init__(self)

        self.socket = socket
        self.address = address
        self.buf_size = 1024

        print "New client is connected!"

    def run(self):
        print "user1 : abc123 = %s" % User.check_login("user1", "abc123")
        print "user1 : abc125 = %s" % User.check_login("user1", "abc125")

        # on exit
        self.socket.close()

if __name__ == "__main__":
    server = MyServer()
    server.run()