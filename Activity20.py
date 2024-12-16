import os 
tama = True
no = 0
while tama == True:
    ask = input("would you like to continue? (yes/no)")
    if ask.lower() == "no":
        print(" Program Terminated")
        break
        ask == False
    else:
        os.system('cls')
        for x in range(1,6):
            no += 1
            for r in range(1,no+1):
                for y in range(1,x+1):
                    print("*",end=" ")
                for z in range (5,x,-1):
                    print(" ",end=" ")
                print()
            continue