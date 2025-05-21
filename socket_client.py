# Import socket module
import socket
import csv
from time import sleep

# database files
hotels = "hotel_list.txt"
reservations = "hotel_reservation.txt"
testFile = "testFile.txt"

# In this Line we define our local host
# address with port number
SERVER = "127.0.0.1"
PORT = 8080
# Making a socket instance
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# connect to the server
client.connect((SERVER, PORT))

''' displays each hotel according to user_choice '''
def printHotel(row):
    r = list(csv.reader([row]))[0]
    print(f'\nHotel: {r[1]}\nCity: {r[2]}, {r[3]}\nRating: {r[4]}\nHotel ID: {r[0]}')  

def printReservation(entry):
	r = list(csv.reader([entry]))[0]
	print(f'Name: {r[0]}\nPhone number: {r[1]}')
	with open(hotels,'r') as f:
		for row in f:
			if r[2] in row:
				printHotel(row)

def cancelReservation(user_name,user_phone,hotelID):
	key_line = f"{user_name},{user_phone},{hotelID}"
	with open(reservations, "r") as f:
		lines = f.readlines()
	with open(reservations, "w") as f:
		for line in lines:
			if line.strip("\n") != key_line:
				f.write(line)
	print("\nYour reservation has been cancelled.")

def viewReservation(user_phone,user_name):
	with open(reservations,'r') as f:
		hasReserved = 0
		for entry in f:
			r = list(csv.reader([entry]))[0]
			if user_phone in entry and user_name in entry:
				print("\nHere is your reservation:")
				hasReserved += 1
				printReservation(entry)
	if hasReserved == 0:			
		print("Sorry, couldn't find your reservation.")

def makeReservation():
	hotelID = input("\nEnter the Hotel ID (#####): ")
	# print("\nEnter your information to reserve your hotel.")
	user_name = input("Enter your name: ")
	user_phone = input("Enter your phone number (###-###-####): ")
	
	r = open(reservations,"a")
	# check_in = input("")
	reserve = f'{user_name},{user_phone},{hotelID}\n'
	r.write(reserve)
	r.close()
	# print(f'You have booked a stay at {check_choice({hotelID})}')
	print("\nThank you for booking with us. :D")

def check_choice(userInput):
	choice_exists=False
	print(f"\nChecking for hotels in {userInput}:")
	avail=0
	with open(hotels,'r') as f:
		for row in f:
			if userInput in row:
				choice_exists=True
				avail+=1
				sleep(.5)
				printHotel(row)
	if avail > 0:
		makeReservation()
	if avail == 0:
		sleep(.5)
		print(f'Sorry! No hotels in {userInput} at the moment.')

def printOptions():
	print("\n1. Make a reservation\n2. View a reservation\n3. Cancel a reservation\n4. Exit\n")

if __name__ == '__main__':

	print("\n ----- Starting Session. -----\n")
	print("Welcome to the Hotel Reservation System!")

	while True:
		
		printOptions()
		userOption = input("What can we help you with? : ")
		if userOption == "4":
			print("Client has exited.")
			break
	
		if userOption == "1":
			user_city = input("What city are you staying in? : ")
			check_choice(user_city)

		if userOption == "2":
			user_name = input("\nPlease enter your name : ")
			user_phone = input("Please enter your phone number (###-###-####) : ")
			viewReservation(user_phone,user_name)

		if userOption == "3":
			user_name = input("\nPlease enter your name : ")
			user_phone = input("Please enter your phone number (###-###-####) : ")
			hotelID = input("Please enter the Hotel ID (#####) : ")
			cancelReservation(user_name,user_phone,hotelID)
  
	print("\n ----- Session has ended. -----")
	client.close()
