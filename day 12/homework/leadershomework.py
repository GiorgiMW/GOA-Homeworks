#Write an algorithm that prints whether a number entered by the user is positive, negative, or zero.
user_number = int(input("Enter number here: "))

if user_number > 0:
    print("Your number is positive")
elif user_number < 0:
    print("Your number is negative")
else:
    print("Your number is zero")