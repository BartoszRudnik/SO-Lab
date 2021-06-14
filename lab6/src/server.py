#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import mysql.connector


def create_tables():

    drop_user_table_query = "DROP TABLE user"

    drop_message_table_query = "DROP TABLE message"

    create_user_table_query = """
    CREATE TABLE user(
        first_name VARCHAR(100) PRIMARY KEY,
        user_password VARCHAR(100)       
    )
    """

    create_message_table_query = """
    CREATE TABLE message(
        message_id INT AUTO_INCREMENT PRIMARY KEY,
        msg VARCHAR(200)
    )
    """

    # cursor.execute(drop_user_table_query)
    # cursor.execute(drop_message_table_query)
    cursor.execute(create_user_table_query)
    cursor.execute(create_message_table_query)
    db.commit()


def sign_up(first_name, user_password):
    insert_user = """
    INSERT INTO user(first_name, user_password)
    VALUES
    ( %s, %s)
    """

    cursor.execute(insert_user, (first_name, user_password))
    db.commit()


def sign_in(first_name, user_password):
    check_user = "SELECT * from user WHERE user.first_name = %s AND user.user_password = %s"

    cursor.execute(check_user, (first_name, user_password))
    result = cursor.fetchall()

    return result != None


def get_message_history(client):
    message_history = "SELECT msg from message WHERE msg LIKE '%:%'"

    cursor.execute(message_history)
    result = cursor.fetchall()

    for message in result:
        message = str(message)

        index = message.index(':')

        if(index != len(message) - 5):
            client.send(bytes(message[2:len(message) - 3] + '\0', "utf8"))


def send_message_to_db(message):
    insert_message = """
    INSERT INTO message(msg)
    VALUES
    (%s)
    """
    cursor.execute(insert_message, (str(message),))
    db.commit()


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(
            bytes("Connection accepted", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    client.send(
        bytes("Enter 1 to sign in, 2 to sign up", "utf8"))
    mode = client.recv(BUFSIZ).decode("utf8")
    client.send(
        bytes("Enter username", "utf8"))
    name = client.recv(BUFSIZ).decode("utf8")
    client.send(
        bytes("Enter password", "utf8"))
    password = client.recv(BUFSIZ).decode("utf8")

    while True:
        if mode == '1':
            if sign_in(name, password):
                get_message_history(client)
                break
            else:
                client.send(
                    bytes("Wrong user or password, try again!", "utf8"))
                client.send(
                    bytes("Enter 1 to sing in, 2 to sign up", "utf8"))
                mode = client.recv(BUFSIZ).decode("utf8")
                client.send(
                    bytes("Enter username", "utf8"))
                name = client.recv(BUFSIZ).decode("utf8")
                client.send(
                    bytes("Enter password", "utf8"))
                password = client.recv(BUFSIZ).decode("utf8")
        elif mode == '2':
            sign_up(name, password)
            get_message_history(client)
            break
        else:
            client.send(
                bytes("Wrong mode, choose 1 or 2!", "utf8"))

            client.send(
                bytes("Enter 1 to sing in, 2 to sign up", "utf8"))
            mode = client.recv(BUFSIZ).decode("utf8")
            client.send(
                bytes("Enter username", "utf8"))
            name = client.recv(BUFSIZ).decode("utf8")
            client.send(
                bytes("Enter password", "utf8"))
            password = client.recv(BUFSIZ).decode("utf8")

    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"), msg)
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"), " ")
            break


# prefix is for name identification.
def broadcast(msg, string_msg, prefix=""):
    """Broadcasts a message to all the clients."""

    encoding = 'utf-8'

    if string_msg != None:

        if isinstance(prefix, bytes):
            prefix = prefix.decode(encoding)

        if isinstance(string_msg, bytes):
            string_msg = string_msg.decode(encoding)

        send_message_to_db(prefix + string_msg)

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)


clients = {}
addresses = {}

db = mysql.connector.connect(
    host="db",
    user="myuser",
    password="mypass",
    database="chat_app_database",
    port="3306"
)
cursor = db.cursor()

create_tables()

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
