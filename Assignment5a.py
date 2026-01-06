# Demonstrate List Slicing.
#create a list of numbers from 1 to 10
number_list = list(range(1,11))
#Extracts the first five elements from the list using slicing
first_five = number_list[:5]
reversed_five = first_five[::-1]
print(number_list)
print(f"Extracted list first five elemnet list : {first_five} ")
print(f"Reversed list of first five element: {reversed_five}")