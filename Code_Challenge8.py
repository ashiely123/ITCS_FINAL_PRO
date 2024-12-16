odd = 0
even = 0
sum = 0
for x in range(1, 11):
    num = eval(input(f"Enter #{x} :"))
    sum += num
    if num % 2 == 0:
        even += num
    else:
        odd += num

print(f"the sum of all the numbers given is {sum}")
print(f"the sum of all the numbers given is {odd}")
print(f"the sum of all the numbers given is {even}")