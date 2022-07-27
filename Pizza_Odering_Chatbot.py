print("Hello, my name is Jarvis your virtual assistant. I will help you order a pizza!")
print("I am going to ask you a few questions. After typing an answer, press enter.")
print("\n")
userName = input("\nEnter your name:  ")
print("\n")
print("\nHello, " + userName + ". Nice to meet you!")
size = input("\nWhat size would you like?  Enter small, medium, or large:  ")
flavor = input("\nEnter the flavor of the pizza:  ")
crustType = input("\nWhat type of crust would you like:  ")
quantity = input("\nHow many of these would you like to order:  ")
quantity = int(quantity)
method = input("\nIs this carr out or delivery:  ")

#Adding computational thinking
salesTax = 1.1
pizzaCost = 14.99
total = (pizzaCost * quantity) * salesTax

print("\n-----------------")
print("Thank you,", userName, ", for your order.")
print("Your", quantity, size, flavor, "pizza with", crustType, "crust costs", "${:,.2f}".format(total) + ".")
print("\n-----------------")
