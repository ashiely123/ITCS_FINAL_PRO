for x in range(1,5):
    for y in range(5,x,-1):
        print("",end="")
    for z in range(1,x):
        print("*",end="")
    for a in range(0,x):
        print("*",end="")
    print()

for x in range(1,6):
    for y in range(1,x):
        print("",end="")
    for z in range(6,x,-1):
        print("*",end="")
    for a in range(5,x,-1):
        print("*",end="")
    print()