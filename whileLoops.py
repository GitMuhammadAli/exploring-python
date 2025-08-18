

# count = 1
# while count <= 5:
#     print(f"Count is: {count}")
#     count = count + 1

# print("-" * 25) # Separator



# user_input = ""
# print("Type 'quit' to exit the loop.")
# while user_input != "quit":
#     user_input = input("Enter something: ")
#     if user_input != "quit":
#         print(f"You entered: {user_input}")

# print("-" * 25) # Separator

# Example 3: Infinite loop with a 'break' statement

# Flow:
# 1. The loop condition is always 'True', so it would run forever without a break.
# 2. The program asks the user for a number.
# 3. The 'int()' function converts the input string to an integer.
# 4. If the user enters a number greater than 10, the 'break' statement is executed.
# 5. The 'break' statement immediately exits the loop, and the program continues.

# print("This loop will run until you enter a number greater than 10.")
# while True:
#     try:
#         number = int(input("Enter a number: "))
#         if number > 10:
#             print("You entered a number greater than 10. Exiting the loop.")
#             break
#         else:
#             print("Please enter a number greater than 10.")
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")



secret = 9
count = 0
user = 3
while user > count:
    num = int(input("guess  "))
    user -=1
    if num == secret:
        print("Win !")
        break
    else:
        print("tryAgain tries left" , user)
    

