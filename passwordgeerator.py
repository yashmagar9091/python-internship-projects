import random
import string
length=int(input("Specify the length of your password:"))
complexity=int(input("enter the complexity :'Easy=1' ,'Medium=2' ,'Hard=3' "))
if(complexity==1):
    def generate_random_number(length):
        if length <= 0:
            raise ValueError("Length must be greater than 0")
    
        min_value = 10 ** (length - 1)
        max_value = (10 ** length) - 1
    
        return random.randint(min_value, max_value)
    password=generate_random_number(length)
    print("Password is:",password)
elif(complexity==2):
    def generate_pass(length):
        characters=string.ascii_letters + str(random.randint(0,10))
        letter=''.join(random.choice(characters) for i in range(length))
        return letter
    password=generate_pass(length)
    print(password)
elif(complexity==3):
    def generate_letter(length):
        characters = string.ascii_letters + string.whitespace + string.punctuation

        letter = ''.join(random.choice(characters) for _ in range(length))

        return letter
    password=generate_letter(length)
    print(password)
    


