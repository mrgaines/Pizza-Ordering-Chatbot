print("Hello, my name is Jarvis your virtual assistant. I will help you order a pizza!")
print("I am going to ask you a few questions. After typing an answer, press enter.")
print("\n")
userName = input("\nEnter your name:  ")
if userName == "jay":
    print("\nMy creator, " + userName + ". Pleasure to serve you!")
else:
    print("\nHello, " + userName + ". Nice to meet you!")
print("\n")
print("\nHello, " + userName + ". Nice to meet you!")
size = input("\nWhat size would you like?  Enter small, medium, or large:  ")
flavor = input("\nEnter the flavor of the pizza:  ")
crustType = input("\nWhat type of crust would you like:  ")
quantity = input("\nHow many of these would you like to order:  ")
quantity = int(quantity)
method = input("\nIs this carr out or delivery:  ")
if method.lower() == "delivery":
    deliveryFee = 5
else:
    deliveryFee = 0

#Adding computational thinking

salesTax = 1.1
pizzaCost = 0
if size.lower() =="small":
    pizzaCost = 8.99
elif size.lower() == "medium":
    pizzaCost = 14.99
elif size.lower() == "large":
    pizzCost = 17.99
total = (pizzaCost * quantity) * salesTax + deliveryFee

print("\n-----------------")
print("Thank you,", userName, ", for your order.")
print("Your", quantity, size, flavor, "pizza with", crustType, "crust costs", "${:,.2f}".format(total) + ".")
if total >= 50:
    print("\nCongratualtions, you've been awarded a $10 off coupon for your next order!")
else:
    print("\nOrders over $50 will recieve a free $10 off coupon!")
print("\n-----------------")
