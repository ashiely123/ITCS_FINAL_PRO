isBuy = input("Do you want make a grocery purchase (yes/no): ")

if isBuy.lower() == "yes" :
	item_name = input("Enter the item name: ")
	item_price = eval(input("Enter the price of the item: "))
	age = eval(input("Enter your age: "))
	cash = eval(input("Enter the amount of cash you have given: "))
    
	discount_amount = round(item_price * 0.060, 4)
	discount_price = round(item_price - discount_amount, 4)
	tax_amount = round(item_price * 0.155, 4)
	tax_price = round(item_price + tax_amount)
    
	if age >= 60:
		print(f"\nHi, our dear customer, you purchased a/an {item_name}, that costs {item_price}Php plus a 5.2% discount {discount_amount}Php to your total purchase. ")
		print(f"Total: {round(item_price - discount_amount, 4)} ")
		print(f"Change: {round(cash - discount_price, 4)} ")
		print("Thank  you for shopping, see you next time! ")

	elif age >=18:
		print(f"\nHello!, you have purchased {item_name}, that costs {item_price}Php plus a 14.3% tax {tax_amount}Php to your total purchase. ")
		print(f"Total: {round(item_price + tax_amount, 4)} ")
		print(f"Change: {round(cash - tax_price, 4)} ")
		print("Thank you for shopping,Hope to see you  next time! ")
	
	else:
		print()
		
else:
	print("\nThank you for shopping with us! we hope to see you again.")