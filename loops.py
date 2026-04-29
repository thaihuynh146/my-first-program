# For Loops

# Loop from 0 to 9
print("=== For Loop (0 to 9) ===")
for i in range(10):
    print(i)

# Loop from 1 to 5
print("\n=== Counting 1 to 5 ===")
for num in range(1, 6):
    print(num)

# While Loop
print("\n=== While Loop ===")
count = 0
while count < 5:
    print("Count:", count)
    count = count + 1

# Loop through a list
print("\n=== Loop Through List ===")
fruits = ["apple", "banana", "orange", "mango"]
for fruit in fruits:
    print("I like", fruit)

# Multiplication table
print("\n=== Multiplication Table of 5 ===")
for i in range(1, 11):
    result = 5 * i
    print(f"5 x {i} = {result}")