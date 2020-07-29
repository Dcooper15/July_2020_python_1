print("What day of the week is it? ")
user_input = int(input("Enter a number 0-6: "))

if user_input == 0:
    print("It is Sunday.")
elif user_input == 1:
    print("It is Monday.")
elif user_input == 2:
    print("It is Tuesday.")
elif user_input == 3:
    print("It is Wednesday.")
elif user_input == 4:
    print("It is Thursday.")
elif user_input == 5:
    print("It is Friday.")
elif user_input == 6:
    print("It is Saturday.")
else:
    print("This is an invalid number. Please enter a number 0-6")