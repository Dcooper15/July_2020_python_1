print("This is a Celsius to Fahrenheit converter!")
user_input = int(input("Please enter a temperture in Celsius: "))

new_fahr_temp = (user_input * 9/5) + 32

print("The temperture of " + str(user_input) + " degrees Celsius, is equivalent to " + str(new_fahr_temp) + " degrees Fahrenheit.")