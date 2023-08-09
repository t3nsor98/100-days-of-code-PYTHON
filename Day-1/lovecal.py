your_name, partners_name = input("What is your name: ") , input("what is your partner's name: ")
name1, name2 = your_name.lower(), partners_name.lower()
full_name = name1 + name2
right_hand_side_number = full_name.count("l") + full_name.count("o") + full_name.count("v") + full_name.count("e")
left_hand_side_number = full_name.count("t") + full_name.count("r") + full_name.count("u") + full_name.count("e")

percentage = str(left_hand_side_number) + str(right_hand_side_number)

print(percentage)