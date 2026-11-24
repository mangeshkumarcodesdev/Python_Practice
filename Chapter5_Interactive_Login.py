# Chapter 4.5 Interactive Login and Result Checker

print("--- Welcome to the Student Portal ---")

# User se username aur password  maangna
username = input("Enter your username: ")
password = input("Enter your password: ")

# Condition checker
if username == "admin" and password == "python123":
    print("\nLogin Successful! Welcome Admin.")
    print("--------------------------------")

    marks = int(input("Enter your marks (0-100): "))
    
    if marks >= 90:
        print("Excellent! Your grade is A+")
    elif marks >= 70:
        print("Good job! Your grade is B")
    elif marks >= 50:
        print("You passed. Your grade is C")
    else:
        print("Sorry, you failed. Better luck next time.")

else:
    print("\nError: Invalid username or password!")
    print("Access Denied.")
