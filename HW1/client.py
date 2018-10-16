#Alex Rodriguez
#Programming Assignment 1
#CST 311

from socket import *
import time
import random

#Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

#create packet
bytes= random._urandom(1024)
#timeout= time.time() + duration


#store time values in array
nums = []
lost = 0

serverSocket.settimeout(1)

#10 packages are sent
for sent in range(1,11):
    try:
        #time stamp
        start = time.time()
        #package is sent
        serverSocket.sendto(bytes,('localhost',12000))

        message,server=serverSocket.recvfrom(1024)
        #ending time stamp
        end= time.time()
	
	diff = end-start
        #store value in array
        nums.append(diff)

        print("Ping", sent, ": ", diff)

    except timeout:
        print ("Request Timed Out")
        lost+=1

print("\n")
print("Minimum: ",min(nums))
print("Maximum: ",max(nums))
print("Average: ", sum(nums)/len(nums))
print("Package Loss Rate: %",lost/len(nums))
