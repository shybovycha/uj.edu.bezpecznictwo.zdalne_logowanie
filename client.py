import socket
import pickle

class MyClient:
    def __init__(self, host = 'localhost', port = 5000):
        self.host = host
        self.port = port
        self.buf_size = 1024
        self.is_logged_in = False

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

    def login(self, username, password):
        self.is_logged_in = False

        command = pickle.dumps({ "command": "login", "username": username, "password": password })

        self.socket.send(command)
        response = self.socket.recv(self.buf_size)

        if response == 'ok':
            self.is_logged_in = True

        return response == 'ok'

    def logout(self):
        command = pickle.dumps({ "command": "logout" })

        self.socket.send(command)
        response = self.socket.recv(self.buf_size)

        if response == 'ok':
            self.is_logged_in = False

        return response == 'ok'

    def change_password(self, new_password):
        command = pickle.dumps({ "command": "chpwd", "new_password": new_password })

        self.socket.send(command)
        response = self.socket.recv(self.buf_size)

        return response == 'ok'

    def run(self):
        # print "user1 : abc123 = %s" % self.login("user1", "abc123")
        # print "user1 : abc124 = %s" % self.login("user1", "abc124")

        print "login: %s" % self.login("user1", "abc123")
        print "chpwd: %s" % self.change_password("abc125")
        print "logout: %s" % self.logout()
        print "login again: %s" % self.login("user1", "abc125")
        print "logout: %s" % self.logout()
        print "login wrongly: %s" % self.login("user1", "abc123")

        # on exit
        self.socket.close()

if __name__ == "__main__":
    client = MyClient()
    client.run()