#infiniti-code
# simple calculator
import time
import sys

def  add (a, b) :  
 return a+b

def  sub (a, b) :  
 return a-b 

def  mul (a, b) :  
 return a*b 

def  div (a, b) :  
 return a//b

print("Simple Calculator!")
print("""Select operation:
1.add  
2.sub
3.mul
4.div or '0' to exit""")
def calci():
    while True:
        choice = int(input("\nenter your choice = "))
        if choice > 4:
            print("enter correct choice!")
            break

        elif choice == 0:
            print("Exiting")
            time.sleep(4)
            sys.exit(1)

        elif choice == 1 or 2 or 3 or 4:

            a = int(input("enter number 1 = "))
            b = int(input("enter number 2 = "))


            if choice == 1:
                print(add(a, b))
                print("...next")

            elif choice == 2:
                print(sub(a, b))
                print("...next")

            elif choice == 3:
                print(mul(a, b))
                print("...next")

            elif choice == 4:
                print(div(a, b))
                print("...next")

calci()
calci()
calci()
calci()
calci()
calci()
calci()
calci()
calci()
calci()
calci()
calci()
calci()




