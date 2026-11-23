# Chapter3: Operator
# Topic: 1.Arithmetic Operators(math)➡️
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b) 
print(a // b)
print(a % b)
print(a ** b)

# Topic: 2. Comparison Operators➡
# Boolean main True ya False
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= 10)
print(a <= b)
# Topic: 3. Assignment Operators(shortcut)➡
x = 10
x += 5   # x = x + 5 → 15
x -= 3   # x = x - 3 → 12
x *= 2   # x = x * 2 → 24
x //= 5  # x = x // 5 → 4
x **= 2  # x = x ** 2 → 16
print(x) # 16

x = 7
x += 3
print(x)
x *= 2
print(x)
x **= 2
print(x)
# Topic: 4. Logical Operators(and, or, not)➡

age = 22
has_id = True

print(age >= 18 and has_id)
print(age < 18 or has_id)
print(not has_id)
a = 10
print(a > 5 and a < 20) 
age = 22
can_vote = True
print(age >= 18 and can_vote)

# Topic: 5. Pracedence Operators
result = 10 + 5 * 2
print(result)
print((10 + 5) * 2)
print(17 // 5)
print(17 % 5)
a = 20 / 5 * 2
print(a)
number = 14
is_even = (number % 2 == 0)
print(is_even)
