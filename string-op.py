print(dir(str))

data = "   Hello World   "
print("Before: ", data)

new_upper = data.upper()
print("Upper Result -> ", new_upper)

new_lower = data.lower()
print("Lower Result -> ", new_lower)

new_strip = data.strip()
print("Strip Result:", new_strip)

equal = "H" == "h"
print("EQUAL H == h ->", equal)

product = "Hindware Smart Appliances | Nadia IN 60 cm Chimney | 1500 CMH |Curved Glass | Filterless | Auto Clean | Touch Control, Motion Sensor | 10 Yrs Warranty on Motor & 2 Yrs on Product (Black) "
# product = product.upper()
# product = product.lower()

# print(product)
result = product.startswith("hindware")
print("Starts With? -?", result)

result = product.find("Chimney")
print("find result ->", result)

print("After: ", data)

print(product)

result = product.split()
print(result)
result = product.split("|")
print(result)


def remove_white_space(data):
    print("IP:", data)
    result = data.strip()
    print("OP:", result)


remove_white_space("  Hello   World  ")
remove_white_space("   This is my string program    ")
remove_white_space("John     ")


def find_id(id):
    all_cards = "aadhaar voter pan passport ration_card"  # -> Large Source String
    return all_cards.find(id)


result = find_id("aadhaar")  # Small Search String
print(result)

print(dir(str))

element_text = " John  ".strip()

if not element_text:
    print("Empty Input Data")


print("Proceed")

"".upper()

"Hello".lower()
