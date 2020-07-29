ninja_turtles = ["Donatello", "Michelangelo", "Leonardo", "Raphael"]


count = 0

print("WHILE LOOP")
while count < len(ninja_turtles):
    print(ninja_turtles[count])
    count += 1


print("FOR LOOP")
for turtle in ninja_turtles:
    print(turtle)
    if turtle == "Leonardo":
        break

    

