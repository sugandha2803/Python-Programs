#Leap year program without using logical operator 

while True:

    yr=int(input("Enter year : "))

    if yr%100==0:
        if yr%400==0:
            print(f"{yr} is leap year ")
        else :
            print("It is a century year \nbut not a leap year")
            
    else:
        if yr%4==0:
            print("Leap year")
        else:
            print("Not a leap year")
            
    check=int(input("\n\n if you want to quit press 0 (0/1) : "))
    if check==0:
        break 
            
