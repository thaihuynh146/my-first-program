# If/Else statements

age = 20

# Simple if statement
if age >= 18:
    print("You are an adult!")

# If/Else
if age >= 18:
    print("You can vote!")
else:
    print("You cannot vote yet!")

# If/Else If/Else
print("\n=== Grade Calculator ===")
grade = 85

if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Comparison operators
print("\n=== Comparison Operators ===")
print("10 > 5:", 10 > 5)      # True
print("10 < 5:", 10 < 5)      # False
print("10 == 10:", 10 == 10)  # True (equal)
print("10 != 5:", 10 != 5)    # True (not equal)

# Your practice: Age checker
print("\n=== Your Age Check ===")
your_age = int(input("Enter your age: "))
if your_age >= 18:
    print("You are an adult")
else:
    print("You are a teenager")
    