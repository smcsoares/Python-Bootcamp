print("Welcome to the rollecoaster!")
height = int(input("What is your height in cm ? "))
age = int(input("What is your age? "))
price = 0

if height >= 120:
    if age < 12:
        price = 7
    elif 12 <= age <= 18 :
        price = 7
    elif 45 <= age <= 55:
        print("Free ride") 
    else:
        price = 12

    opt = input("Do you want photos? (Y/N) ")

    if opt == 'Y':
        price += 3

    print(f"You can ride the rollercoaster for ${price}")
else:
    print("Sorry you have to grow taller before you can ride.")



num_to_check = int(input("What is the number you want to check?"))

if num_to_check % 2 == 0:
    print("Number is even")
else:
    print("Number is not even")
    