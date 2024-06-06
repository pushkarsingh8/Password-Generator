#Password Generator:-
import random
import string

#Function to generate a password of given length
def generate_passw(length):
    
    special_charcters = "@!&*/_~'#^%-"
    captial = random.choice(string.ascii_uppercase)
    number = str(random.randint(1,9))
    
    #Empty variable
    password = ""

    for _ in range(length-3):

        password +=random.choice(string.ascii_lowercase)

    password += password
    password += random.choice(special_charcters)
    password +=captial+number

    #shuffle all character in password variable
    password = "".join(random.sample(password,length))
    
    return password

#Error handling 
while True:
    try:    
        l = int(input("Enter Password Length: "))
        break
    except ValueError:
        print("invalid input. Please enter integer value:")

print("Your Password is ",generate_passw(l))