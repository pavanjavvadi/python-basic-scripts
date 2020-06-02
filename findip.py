#This program is used to find out the ip and hostname

import socket #importing the socket module

hostname = socket.gethostname() #getting the host name by using socket.gethostname() method
ip_address = socket.gethostbyname(hostname) #this is used to find the ip_address

print(f"ip-address : {ip_address}")
print(f"hostname : {hostname}")
