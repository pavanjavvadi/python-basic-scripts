#This is a python program for find out the reverse of a number
num = int(input("Enter the number: "))
temp = num
reverse = 0
while num > 0:
    digit = num % 10 # This is used t find the remainder of the number
    reverse = (reverse*10) + digit  #This logic helps in finding the reverse of the number
    num = num//10 #This is used to find the quotient of a number

print(f"reverse of the number {num} is : {reverse}") #This print out the reverse of a number


