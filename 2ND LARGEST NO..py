def second_largest_sorting(nums):
    unique_nums = list(set(nums))  # Remove duplicates
    if len(unique_nums) < 2:
        return None  # No second largest if fewer than 2 unique elements
    unique_nums.sort(reverse=True)
    return unique_nums[1]

# Example usage
numbers = [10, 20, 4, 45, 99, 99]
print("Second largest number (sorting):", second_largest_sorting(numbers))
