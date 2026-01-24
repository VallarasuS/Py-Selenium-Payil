# def check_temp(temp):
#     # if temp < 21:
#     #     print("The temp is COLD")
#     # else:
#     #     if temp >= 21 and temp <= 24:
#     #         print("The temp is NORMAL")
#     #     else:
#     #         if temp > 24:
#     #             print("The temp is HOT")

#     if temp >= 21 and temp <= 24:
#         print("Normal")
#     elif temp > 24:
#         print("Hot")
#     else:
#         print("Cold")


# def metal(metal_name):

#     # metal_name = metal_name.lower()  # -> gold
#     metal_name = metal_name.upper()  # -> GOLD

#     if metal_name == "GOLD":
#         print("The price of Gold rate is 1800")
#     elif metal_name == "SILVER":
#         print("The price of Silver rate is 1000")
#     elif metal_name == "PLATINUM":
#         print("The price of Platinum rate is 5000")
#     else:
#         print("Invalid")


# metal("gold")
# metal("silver")
# metal("iron")

# Truthy Falsy
# 0, "", None -> False

x = None
y = 2
# is_x_greater = x > y

if x:
    print("True")
else:
    print("False")
