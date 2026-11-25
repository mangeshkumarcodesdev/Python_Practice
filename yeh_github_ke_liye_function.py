# Topic 1: Basic Funcction

def say_hello():
    print("Hello! Welcom to Python.")

say_hello()
say_hello()
# Topic 2: Function with Parameters(Input)

def great_user(name):
    print("Hello,", name, "! How are you?")

great_user("Mangesh")
great_user("rahul")
# topic 3: Functionwith Return value (Output)

def add_numbers(a, b):
    result = a + b
    return result

my_total = add_numbers(10, 5)
print("The total is:", my_total)
