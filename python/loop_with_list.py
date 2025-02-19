fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")


# for loop with else
for fruit in fruits:
    if fruit == "Apple":
        print("Found Apple!")
        break
else:
    print("No Apple found in the fruits list")


# while loop with else
count = 0
while count < 5:
    print(count)
    count += 1

else:
    print("Count is not less than 5")
