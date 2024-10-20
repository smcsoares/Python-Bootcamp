s_price = 15 
m_price = 20
l_price = 25
bill = 0

print("Welcome to Python Pizza Deliveries!")
size = input("What size do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese ? Y or N: ")


if size == "S":
    bill += s_price
elif size == "M":
    bill += m_price
elif size == "L":
    bill += l_price
else:
    print("You typed the wrong inputs")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is {bill}")