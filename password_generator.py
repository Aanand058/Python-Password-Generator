import random

alphabets="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!@#$%^&*()?"

letterLen = int(input("Enter how many letters you want in your password: "))
numLen = int(input("Enter how many digits you want in your password: "))
symbolLen = int(input("Enter how many symbols you want in your password: "))

#Generating different variations of required password
p1 = "".join(random.sample(alphabets,letterLen))
p2 = "".join(random.sample(numbers,numLen))
p3 = "".join(random.sample(symbols,symbolLen))

#Printing the combined password
print(p1+p2+p3)
