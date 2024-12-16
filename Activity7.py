AA = input("What's your name, miner? ")
print("\n")
A = 0
B = input("Have you mined today? ")
print("\n")

if B.upper() == "YES":
        C = eval(input("How many Golds did you mined? "))
        print("\n")
        D = A + C
        print("Congratulations! ",AA,"You have mined ", D," golds, today")
elif B.upper() != "YES":
        print("\n")
        print("That's unfortunate, ",AA,"you've mined ", A, "golds today")
        print(" you should mine more efficient ", AA)