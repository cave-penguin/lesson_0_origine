my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)

my_foods.append("cannoli")
friend_foods.append("ice cream")
# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)

print(f"The first three items on the list are: {my_foods[: 4]}")
print(
    f"Three items from the middle of the list are: {
      friend_foods[len(my_foods) // 2 - 1:len(my_foods) // 2 + 2]}"
)
print(f"The last three items in the list are: {my_foods[-3:]}")
