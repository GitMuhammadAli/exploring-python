# --- Conditional Statements in Python ---

# This code block demonstrates how conditional statements work.
# A conditional statement checks if a condition is True and executes the corresponding code.

# Example 1: Basic if-else statement

age = 20

# Flow: The program first checks if 'age' is less than 18.
# If True, it prints the first message.
# If False, it skips the 'if' block and goes to the 'else' block, printing the second message.
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")

print("-" * 25) # Separator

# Example 2: if-elif-else statement (Multiple conditions)

score = 85

# Flow: The program checks each condition in order from top to bottom.
# It checks 'score >= 90'. If True, it prints "Excellent!" and stops.
# If False, it checks the next condition, 'score >= 80'.
# If that is True, it prints "Good job!" and stops.
# If all 'if' and 'elif' conditions are False, it executes the 'else' block.
if score >= 90:
    print("Grade: A - Excellent!")
elif score >= 80:
    print("Grade: B - Good job!")
elif score >= 70:
    print("Grade: C - You passed.")
else:
    print("Grade: F - You should try again.")

print("-" * 25) # Separator

# Example 3: Nested if statements

temperature = 25
is_raining = True

# Flow: An outer 'if' checks if the temperature is warm.
# If that condition is True, the code inside the block runs.
# The inner 'if' then checks if it's raining.
# Both conditions must be met for the final "Stay indoors" message to print.
if temperature > 20:
    print("It's a warm day.")
    if is_raining:
        print("It is also raining. Maybe stay indoors.")
    else:
        print("It is not raining. Enjoy the day outside!")
else:
    print("It's a bit chilly.")



print("enter your credit")
credits = input("enter credit between good and bad: ")
downPayment = 0
housePrice = 1000000
if credits == "good":
    downPayment = 0.1 * housePrice
else:
    downPayment = 0.2 * housePrice

print(f"house down payment is {downPayment}")