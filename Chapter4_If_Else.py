# Chapter 4. If-Else (Conditions)
# Example 1. Voting eligibity
age = 20

if age >= 18:
    print("You are an adult.")
    print("You can vote!")
else:
    print("You are a minor.")
    print("You cannot vote yet.")

print("\n----------------------\n")

# Example 2. Chacking password
password = "python123"

if password == "python123":
    print("Login successful! Welcome.")
else:
    print("Error: Incorrect password!")

print("\n-----------------------\n")

# Example 3. If-Elif-Else (Multiple conditions)
marks = 40

if marks >= 90:
    print("Grade: A+")
elif marks >= 70:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
