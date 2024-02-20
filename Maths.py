def greet(name):
    print(f"Hello, {name}")

def special_op(x=1, y=1, z=0):
    return x * y + z

greet("Alice")


result = special_op(2, 3, 4)
print(result)

result = special_op(2, 3)
print(result)

result = special_op()
print(result)

result = special_op(z=2, x=3, y=4)
print(result)

