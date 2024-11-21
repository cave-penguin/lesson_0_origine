# cars = ["audi", "bmw", "subaru", "toyota"]
# for car in cars:
#     if car == "bmw":
#         print(car.upper())
#     else:
#         print(car.title())


# car = "subaru"
# print("Is car == 'subaru'? I predict True.")
# print(car == "subaru")
# print("\nIs car == 'audi'? I predict False.")
# print(car == "audi")

available_toppings = [
    "mushrooms",
    "olives",
    "green peppers",
    "pepperoni",
    "pineapple",
    "extra cheese",
]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")
