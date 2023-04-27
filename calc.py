import math as mt
print("---Calculator using python---")
print("list of operator")
while True:
    print("+  -  *  /  sin   cos  tan  pwr  sqrt  %")
    opt=input("enter the operator:-")

    if(opt=="+"):
        n1=int(input("enter 1st no:-"))
        n2=int(input("enter 2nd no:-"))
        print(n1+n2)
    elif(opt=="-"):
        n1=int(input("enter 1st no:-"))
        n2=int(input("enter 2nd no:-"))
        print(n1-n2)
    elif(opt=="*"):
        n1=int(input("enter 1st no:-"))
        n2=int(input("enter 2nd no:-"))
        print(n1*n2)

    elif(opt=="/"):
        n1=int(input("enter 1st no:-"))
        n2=int(input("enter 2nd no:-"))
        print(n1/n2)
    elif(opt=="sqrt"):
         n=int(input("enter no:-"))
         print(mt.sqrt(n))
    elif(opt=="pwr"):
        n=int(input("enter no:-"))
        n1=int(input("enter how much power you want:-"))
        print(n**n1)
    elif(opt=="sin"):
        n=int(input("enter degree:-"))
        print(mt.sin(n))
    elif(opt=="cos"):
        n=int(input("enter degree:-"))
        print(mt.cos(n))
    elif(opt=="tan"):
        n=int(input("enter degree:-"))
        print(mt.tan(n))
    elif(opt=="%"):
        n=int(input("enter no:-"))
        n1=int(input("enter percentage value:-"))
        print((n*n1)/100)
    else:
        print("select right operator")
    
    



