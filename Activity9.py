A = eval(input("Enter Age ---------->"))

if A >= 1 and A<= 7:
    print("toddler")
elif A >= 8 and A <= 13:
    print("pre teen")
elif A >= 14 and A <= 18:
    print("teenager")
elif A >= 19 and A <= 31:
    print("early adulthood")
elif A >= 32 and A <= 45:
    print("mid adulthood")
elif A >= 46 and A <= 59:
    print("post adulthood")
elif A >= 60 and A <= 100:
    print("senior")
elif A >= 100:
    print("Ancient")