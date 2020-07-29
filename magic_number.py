magic_number = 5

print("Welcome to the Guess A Number Game!")
user_input = int(input("Enter a number between 0 and 25: "))
if user_input == magic_number:
   print("You are a mind reader!")
elif user_input > 5:
    print("Guess was too high.")
else:     
    print("Guess was too low.")
