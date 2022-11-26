b=input("Welcome to the cake cutting program enter whatever you want")
print("press 1:if you want unequal pieces")
print("press 2:if you want equal pieces")
ch=input()
n=int(input("Enter the number of pieces you want:"))

if ch=="1":
    print("press 1:if you want each piece to be of different size")
    print("press 2:if you want pieces of different size but some can be of same aswell")
    s=input()
    if s=="1":
        if n<27 or n<=26:
            print("It is possible")
        else:
            print("not possible")
    elif(s=="2"):
        if n<=360:
            print("Its possible")
        else:
            print("not possible")
elif(ch=="2"):
    if 360%n==0:
        print("Possible ")
    else:
        print("not possible")

