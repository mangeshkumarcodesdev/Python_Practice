# Chapter 7: Lists

fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0])
print(fruits[2])

fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)

fruits = ["apple", "banana", "cherry"]
print(len(fruits))
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
