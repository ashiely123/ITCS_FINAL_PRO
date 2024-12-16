t = int(input("Enter a number range: "))
for x in range(1,t):
    for a in range(1,x,1):
        print(" ",end="  ")
    for b in range(t,x,-1):
        print("* ",end=" ")
        