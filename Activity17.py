A = int(input("Enter a Value"))
for x in range(1,11):
    for y in range(1,A+1):
        print(f"{x} x {y} = {x*y}",end=" \t ")
    print()