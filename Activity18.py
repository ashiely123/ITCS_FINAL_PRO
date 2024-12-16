A = int(input("enter a value:"))
for x in range(1,6):
    for r in range(1,A+1):
        for y in range(1,x+1):
            print("*",end=" ")
        for z in range(x,6):
            print(" ",end=" ")
    print()