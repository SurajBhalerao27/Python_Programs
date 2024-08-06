my_list = [4,5,8,5,-9,4,6,-9,45,65,8,7,9]
print(f'length of list is {len(my_list)}')

# Finding the maximum value in the list
max_value = max(my_list)
print(f'Maximum value in the list is {max_value}')

# Finding the minimum value in the list
min_value = min(my_list)
print(f'Minimum value in the list is {min_value}')

# Finding the average value in the list
avg_value = sum(my_list) / len(my_list)
print(f'Average value in the list is {avg_value}')

# Finding and remove duplicates from the list
new_list = list(set(my_list))
print(f'After removing duplicates : {new_list}')

# Find second last number of list 
if len(my_list) > 2:
    my_list.sort()
    second_last  =  my_list[-2]
else: 
    second_last = None
print(f'Second last number of list is {second_last}')