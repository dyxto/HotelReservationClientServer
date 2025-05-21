# Import socket module
import socket
from threading import Thread
import csv
# from socket_client import user_city, userOption

# database files
hotels = "hotel_list.txt"
reservations = "hotel_reservation.txt"
testFile = "testFile.txt"

# Here we use localhost ip address
# and port number
LOCALHOST = "127.0.0.1"
PORT = 8080
# calling server socket method
server = socket.socket(socket.AF_INET,
					socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)
print("Server started")
print("Waiting for client request..")

def new_client(clientConnection, clientAddress):
    msg = ''
    # Running infinite loop
    while True:
        # server recieves client message
        data = clientConnection.recv(1024)
        msg = data.decode()
        
        # print(f"server received a message! {msg}")

        if msg == "4":
        # makeReservation()
            print("\nOK QUIT\n")
            break


        # result = "\nUnexpected input.\n"
        # output = str(result)
        # clientConnection.send(output.encode())
    
    print("Client Disconnected :", clientAddress)
    clientConnection.close()
    thread.join()
    


# client_list = []
# Here server socket is ready for
# get input from the user
if __name__ == "__main__":
    while True:
        clientConnection, clientAddress = server.accept()
        print("Connected client :", clientAddress)
        thread = Thread(target=new_client,args=(clientConnection,clientAddress))
        thread.start()