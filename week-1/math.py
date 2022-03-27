# add two numbers
def add(x, y):
    return x + y

# subtract two numbers
def sub(x, y):
    return x - y

# multiply two numbers
def mul(x, y):
    return x * y

# divide two numbers
def div(x, y):
    return x/y

if __name__ == "__main__":
    x = 1
    y = 2
    print(f"{x} + {y} = {add(x, y)}")
    print(f"{x} - {y} = {sub(x, y)}")
    print(f"{x} * {y} = {mul(x, y)}")
    print(f"{x} / {y} = {div(x, y)}")