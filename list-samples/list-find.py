def click(button):
    print(button + " Clicked")


buttons = ["Save", "Submit", "Clear", "Help"]


def find(key):
    for b in buttons:
        if b == key:  # Save
            return b


x = find("Save")
click(x)

x = find("Help")
click(x)
