import random

print("welcome to maths game quiz\n\n\n\n play this you will have fun and also it will give positive impact on you calculation speed")
i=1
while(i!=0):

    a= random.randint(1, 1000)
    b= random.randint(1, 100)

    add=a+b
    sub=a-b
    mult=a*b
    div=a/b

    ch=[add,sub,mult]

    d=random.choice(ch)
    if (d==add):
        print(f"solve the quiz \n {a}+{b} = ?")
        ans=a+b

    elif (d==sub):
        if(a>b):
         print(f"solve the quiz \n {a}-{b} = ?")
         ans=a-b
        else:
         print(f"solve the quiz \n {b}-{a}")
         ans=b-a

    elif (d==mult):
        print(f"This ques is a lil bit hard ..........solve the quiz \n {a}*{b} = ?")
        ans=a*b

        '''elif (d==div):
        if(a>b):
         print(f"solve the quiz \n {a}/{b} = ?")
         ans=a/b
        else:
         print(f"solve the quiz \n {b}/{a}")
         ans=b/a'''

    else:
        print(" error in code ")

    f = int(input("enter your answer : "))

    if(f!=ans):
        print("wrong answer \n\n\n start again(run the code)")
        i=0
    else:
        print("right answer")
        
        
        g=int(input("press 1 if you want to play or press 0 for exit : "))
        if(g==0):
            print("well played ")
            i=0
        else:
            i=1
