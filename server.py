import socket
import md5
import threading
import pickle

class User:
    users = {
            "user1": "abc123",
            "user2": "password_123",
            "user3": "password_abc"
        }

    @staticmethod
    def check_login(username, password):
        return (username in User.users and User.users[username] == password)

    @staticmethod
    def change_password(username, new_password):
        User.users[username] = new_password

class MyServer:
    def __init__(self, host = 'localhost', port = 5000):
        self.host = host
        self.port = port
        self.backlog = 5
        self.buf_size = 1024
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

        self.is_logged_in = False

        print "New client is connected!"

    def run(self):
        try:
            while True:
                data_str = self.socket.recv(self.buf_size)

                # empty data received
                if not data_str:
                    break

                data = pickle.loads(data_str)

                if not ("command" in data):
                    raise Exception("Invalid packet")

                if (data["command"] == "login"):
                    if not ("username" in data and "password" in data):
                        #raise Exception("Invalid login arguments")
                        self.socket.send("invalid login arguments")
                        continue

                    is_login_correct = User.check_login(data["username"], data["password"])

                    if (is_login_correct):
                        self.username = data["username"]
                        self.is_logged_in = True

                        self.socket.send("ok")
                    else:
                        self.socket.send("error")
                        self.is_logged_in = False
                elif (data["command"] == "logout"):
                    self.is_logged_in = False
                    self.socket.send("ok")
                elif (data["command"] == "chpwd"):
                    if not self.is_logged_in:
                        # raise Exception("You are not logged in")
                        self.socket.send("you are not logged in")
                        continue

                    if not ("new_password" in data):
                        #raise Exception("Invalid chpass arguments")
                        self.socket.send("invalid chpass arguments")
                        continue

                    User.change_password(self.username, data["new_password"])

                    self.socket.send("ok")
        finally:
            # on exit
            self.socket.close()

if __name__ == "__main__":
    server = MyServer()
    server.run()