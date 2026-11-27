# Topic 1: Tuple
fruits = ("apple", "banana", "mango")
numbers = (10, 20, 30, 40)
mixed = ("Mangrsh", 22, 5.6, True)
empty = ()

print(fruits)
print(type(fruits))

a = (5)
b = (5,)
print(type(a))
print(type(b))

fruits = ("apple", "banana", "mango", "orange")
print(fruits[0])
print(fruits[2])
print(fruits[-1])
print(fruits[-2])

# Topic 2: Slicing
# Format: tuple[start:stop:step]
nums = (10, 20, 30, 40, 50, 60)
print(nums[1:4])
print(nums[:3])
print(nums[3:])
print(nums[::2])
print(nums[::-1])

# Topic 3: Immutable (Unchangeble)
fruits = ("apple", "banana")

fruits = ("grapes",) + fruits[1:]
print(fruits)
# Topic 4: Useful Operation (count() and index()
t = (1, 2, 3, 2, 2)
print(len(t))
print(t.count(2))
print(t.index(3))
print(3 in t)
print(max(t), min(t), sum(t))
print((1, 2) + (3, 4))
print(("Hi",) * 3)

# Packing
person = ("Mangesh", 22, "Azamgarh")

# Unpacking
name, age, city = person
print(name)
print(age)
print(city)

# Swap trick
a, b = 10, 20
a, b = b, a
print(a, b)

# Topic 5: Nested tuple and loop
data = ((1, 2), (3, 4), (5, 6))
print(data[1])
print(data[1][0])

for fruits in ("apple", "banana", "mango"):
    print(fruits)

t = (10, 20, 30, 40, 50)
print(t[-2])
print(t[1:4])

print(type((7)))
print(type((7,)))
print(("a", "b") * 2)

# Count how many times 5 appears in the tuple
t = (5, 3, 5, 8, 5)
print(t.count(5))

# Find the index of 8
print(t.index(8))

x, y, z = (1, 2, 3)
print(y)

# Total number of days
days = ("Mon", "Tue", "Wed")
for day in days:
    print(day)
    print(len(days))
# This causes TypeError: tuples are immutable.
t = (1, 2, 3)
t[0] = 100
