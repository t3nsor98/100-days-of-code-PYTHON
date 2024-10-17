my_array = [64, 34, 25, 12, 22, 11, 90, 5]

len_of_array = len(my_array)
# print(len_of_array)

for i in range(len_of_array):
    for j in range(len_of_array - i - 1):
        if my_array[j] > my_array[j+1]:
            my_array[j],my_array[j+1] = my_array[j+1],my_array[j]
            
            
print(F"Sorted Array: {my_array}")