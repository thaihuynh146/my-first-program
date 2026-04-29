# String operations

text1 = "Hello"
text2 = "World"

# Concatenation (joining strings)
message = text1 + " " + text2
print(message)

# Repeat string
repeated = "Ha" * 3
print(repeated)  # Prints: HaHaHa

# String length
name = "thaihuynh146"
length = len(name)
print("Your name has", length, "characters")

# Upper and lower case
sentence = "I am learning Python"
print(sentence.upper())
print(sentence.lower())

# Replace text
new_sentence = sentence.replace("Python", "JavaScript")
print(new_sentence)

# Extract part of string (slicing)
print("\n=== String Slicing ===")
text = "PYTHON"
print(text[0])      # First character: P
print(text[0:2])    # First 2 characters: PY
print(text[-1])     # Last character: N
