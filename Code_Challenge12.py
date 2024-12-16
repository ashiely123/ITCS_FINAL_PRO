for x in range(1,5):
    for y in range(5, x, -1):
        print("", end="")
    for z in range(1, x):
        print("*", end="")
    for a in range(1,x):
        print("*", end="")
    print()

for i in range(x):
    for j in range(x-1):
        print("", end="")
    print("* * *")