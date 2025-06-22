# Example list
my_list = [1, 2, 3, 4, 5]

# Reversing using a loop
start = 0
end = len(my_list) - 1

while start < end:
    # Swap elements
    my_list[start], my_list[end] = my_list[end], my_list[start]
    start += 1
    end -= 1

print("Reversed list:", my_list)
