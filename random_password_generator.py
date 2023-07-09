#Code for random password generator...

import random
import string 

print("welcome to.password.generator ")

length =int(input("enter the length of the password : "))

low= string.ascii_lowercase 
uper= string.ascii_uppercase
num=string.digits
#symbol=string.punctuation
all= low+uper+num

temp= random.sample(all,length)
password= "".join(temp) 

print(password)