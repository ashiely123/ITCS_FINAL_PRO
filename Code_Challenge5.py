print("Welcome to AJ's Bank Deposit PH")
print("----------------------------------------------------------------------------------------------------------------------------------")
money = eval(input("Please enter your deposit amount:"))

print (f"Your deposit amount is {money}")

th = money//1000
fh = money - (th*1000)
fh2 = fh//500
toh = fh - (fh2*500)
toh2 = toh//200
oh = toh - (toh2*200)
oh2 = oh//100
ff = oh -(oh2*100)
ff2 = ff//50
to = ff - (ff2*50)
to2 = to//20
ten = to - (to2*20)
ten2 = ten//10
five = ten - (ten2*10)
five2 = five//5
one = five - (five2*5)
one2 = one//1


print ("The denomination of your deposit is:")

print (th,"- 1000")
print (fh2,"- 500")
print (toh2,"- 200")
print (oh2,"- 100")
print (ff2,"- 50")
print (to2,"- 20")
print (ten2,"- 10")
print (five2,"- 5")
print (one2,"- 1")