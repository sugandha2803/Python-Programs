def Factorial(num):
    if num==1 or num==0:
        return 1
    else:
        return num*Factorial(num-1)

print("Hello!!\n")
while True:
    num=int(input("Enter a number  to calculate factorial :  "))
    print(f" Factorial of {num} is { Factorial(num)}")
   
    check=bool(input("\n if you want to quit press 0 (0/1) :  "))
    if check==0:
         break
         
       
 