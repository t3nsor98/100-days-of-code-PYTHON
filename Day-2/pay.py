names = input("Input your names divided by commas: ")
new_names = names.split(",")
import random
random_number = random.randint(0,(len(new_names)-1))
print(f"{new_names[random_number]} will pay the bill")