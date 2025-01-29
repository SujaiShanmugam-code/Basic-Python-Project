import random

print("\nWelcome to Sujai's Random Password Generator!")

random_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&_"


numberofpassword = int(input("\nPlease Enter The Number of Passwords to be Generated: "))
password_length = int(input("\nPlease Enter the Length of The Password Needed: "))

print("\nHere are your random passwords: \n")

# Generate the passwords
for x in range(numberofpassword):
    passwords = ""
    for y in range(password_length):
        passwords = passwords + random.choice(random_characters)


    print(passwords)
print("\nPaldies, Sujai's Random Password Generator!")
