def solve_substring_task(N, substrings, main_string, K):
    def can_form_substring(substring, target, deletions_left):
        # Try to form the target substring from the given substring
        i, j = 0, 0
        deletions_used = 0

        while i < len(target) and j < len(substring):
            if substring[j] == target[i]:
                i += 1
                j += 1
            else:
                # Try to delete this character
                if deletions_used < deletions_left:
                    deletions_used += 1
                    j += 1
                else:
                    # Cannot delete more characters
                    break

        # Check if we successfully formed the entire target substring
        return i == len(target), deletions_used

    # Check if any character in main string is missing from all substrings
    all_chars = set("".join(substrings))
    if any(char not in all_chars for char in main_string):
        return "Impossible"

    # Try to form the main string
    current_string = ""
    deletions_remaining = K

    for i in range(len(main_string)):
        found_match = False

        # Try each substring to match the next character
        for substring in substrings:
            possible, deletions_used = can_form_substring(
                substring,
                main_string[i : i + len(main_string) - len(current_string)],
                deletions_remaining,
            )

            if possible:
                current_string += main_string[i]
                deletions_remaining -= deletions_used
                found_match = True
                break

        # If no substring can form the next character
        if not found_match:
            break

    # Determine output based on how much of the string was formed
    if current_string == main_string:
        return "Possible"
    elif len(current_string) == 0:
        return "Nothing"
    else:
        return current_string


# # Input processing
# N = int(input())
# substrings = [input().strip() for _ in range(N)]
# main_string = input().strip()
# K = int(input())

# # Solve and print result
# result = solve_substring_task(N, substrings, main_string, K)
# print(result)


# Input from the example
N = 8
substrings = ["ruined", "goat", "started", "stray", "goal", "get", "nemo", "earring"]
main_string = "getstringsring"
K = 10

# Run the function and print the result
result = solve_substring_task(N, substrings, main_string, K)
print(result)  # Expected output: getstringsr
