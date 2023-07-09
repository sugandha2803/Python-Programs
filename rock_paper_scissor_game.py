import random
print("welcome to the game rock paper scissor \n computer vs you\n\n r=rock\np=papr\ns=scissor\n")
i=1
while(i!=0):

    def result(com,you):
        if(com==you):
            print("this game is tie")
            return "none"
            
            
        elif (com=="r"):
            if(you=="p"):
               return "true"
            elif(you=="s"):
               return "false"
          
        elif (com=="p"):
        
            if(you=="s"):
               return "true"
            elif(you=="r"):
               return "false"
          
        elif (com=="s"):
             if(you=="r"):
                return "true"
             elif(you=="p"):
                return "false"

    c= random.randint(1, 3)
    if(c==1):
        com= "r"
    elif(c==2):
        com= "p"
    elif(c==3):
        com= "s"

    print("computer turn : rock(r) paper(p) scissor(s) : * ")
    you=input("your turn : rock(r) paper(p) scissor(s) :  ")

    if(you=="r" or you=="s" or you=="p" ):
        pass
    else:
        print("give the right input ")
        continue 

    print(f"computer choose : {com}")
    print(f"you choose : {you}\n")
    
    game = result(com,you)
    
         
        
        
    if(game=="true"):
       print ("you win")
    elif(game=="false"):
       print("you loose")
    else:
       print("play again ")


    i=int(input("if you want to exit press 0 otherwise 1  : ")) 
    if(i==0):
         print("exit")
    else:
        print("\n\n")
