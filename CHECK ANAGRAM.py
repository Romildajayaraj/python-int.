def are_anagrams_sorted(s1, s2):
    return sorted(s1) == sorted(s2)

# Example usage
print(are_anagrams_sorted("listen", "silent"))  # True
print(are_anagrams_sorted("hello", "world"))    # False
