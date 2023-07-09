import random
print("rules of game :\n1.computer will choose a number between (1,100), you have 5 chances to guess that number\n2.computer will give you hints that the number you have guessed is greater or lower than the number\n ")
b=1

while(b!=0):

    num=random.randint(1,100)
    print("computer have choose the number  now you guess the number   ")


    for i in range(1,6):
        user=int(input("enter your guess number: "))
        if(user==num):
            print(" hurrahh!!1 you guess the correct answer ")
            break
        else:
            print("wrong answer")
        
            if(user>num):
                    print(f"the number is lower than your guess number (num<{user})")
            elif(user<num):
                    print(f"the number is greater than your guess number (num>{user})")
                
            print(f"you have{5-i} chances left to guess the number\n ")
            if((5-i)==0):
                print("you loose")
                print(f"the number is {num}")
     
               
    b=int(input("if you want to play again press 1(0/1) :  "))