print("Welcome to the tip calculator")

total = float(input("What was the total bill ? "))

tip = int(input("How much tip would you like to give ? 10, 12 or 15 ?"))

n_people = int(input("How many people to split the bill ? "))

final_bill = total * (1 + tip / 100) / n_people

print(f"Each person should pay {final_bill:.2f}")