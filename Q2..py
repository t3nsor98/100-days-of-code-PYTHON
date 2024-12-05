def max_substrings_removed(main_string, substrings):
    if not substrings:
        return 0

    maximum_removals = 0
    for substring in substrings:
        if substring in main_string:
            new_string = main_string.replace(substring, "", 1)
            remaining_substrings = substrings.copy()
            remaining_substrings.remove(substring)
            removals = 1 + max_substrings_removed(new_string, remaining_substrings)
            maximum_removals = max(maximum_removals, removals)

    return maximum_removals


# Example 1
N = 6
substrings = ["hd", "el", "llo", "wor", "ell", "lds"]
main_string = "helloworlds"

# result
result = max_substrings_removed(main_string, substrings)
print(result)  # Output: 4

# Example 2
N = 7
substrings = ["ggc", "rm", "oo", "le", "glh", "oog", "ec"]
main_string = "googlechrome"

# result
result = max_substrings_removed(main_string, substrings)
print(result)  # Output: 3
