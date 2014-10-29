import socket
import md5

class MyClient:
    def __init__(self, host = 'localhost', port = 5000):
        self.host = host
        self.port = port
        self.buf_size = 1024
        self.is_logged_in = False

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

    def encode_password(self, password):
        return md5.new(password).digest()

    def login(self, username, password):
        self.is_logged_in = False

        command = "LOGIN '%s' : '%s'" % (username, self.encode_password(password))

        self.socket.send(command)
        response = self.socket.recv(self.buf_size)

        if response == 'OK':
            self.is_logged_in = True

    def run(self):
        #self.socket.send('Hello, world')
        #data = self.socket.recv(self.buf_size)
        print "user1 : abc123 = %s" % self.login("user1", "abc123")
        print "user1 : abc124 = %s" % self.login("user1", "abc124")

        # on exit
        self.socket.close()

if __name__ == "__main__":
    client = MyClient()
    client.run()