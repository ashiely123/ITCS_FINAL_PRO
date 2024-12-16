for x in range(1,11,1):
    print(end="")
    for y in range(x,11,1):
        print(end=" ")
    print("* " * x)
    for b in range(11,x,-1):
        print(end=" ")
    print("* " * x)