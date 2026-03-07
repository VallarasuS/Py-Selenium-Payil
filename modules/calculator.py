# package
# __init__.py

# - every file is a module
# - every folder is a package


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


if __name__ == "__main__":
    total = add(10, 20)
    print("Calculator: add", total)

    print("Calculator name:", __name__)
