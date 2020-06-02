#this is a program for sum of digit
num = int(input("Enter any number:"))
sum = 0
temp = num
while int(num) > 0:
    digit = (num % 10) # this is used to find the remainder
    sum = sum + digit #this is used o find the sum of a number
    num = num//10 #this is used to find the quotient of the number
print(f"sum of the given number {temp} is : {sum}")