def XfromY(X, Y, S, R):
    n = len(X)
    m = len(Y)

    Y_rev = Y[::-1]

    dynamic_array = [float("inf")] * (n + 1)
    dynamic_array[0] = 0  # No cost to start

    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = X[i:j]
            
            # Check if the substring exists in Y
            if substring in Y:
                dynamic_array[j] = min(dynamic_array[j], dynamic_array[i] + S)
            
            # Check if the substring exists in reversed Y
            if substring in Y_rev:
                dynamic_array[j] = min(dynamic_array[j], dynamic_array[i] + R)

    if dynamic_array[n] == float("inf"):
        return "Impossible"
    else:
        return dynamic_array[n]

# Test cases

# Example 1
X1 = "inveditla"
Y1 = "lavedithnia"
S1, R1 = 3, 5
result1 = XfromY(X1, Y1, S1, R1)
print(f"Result for Example 1: {result1}")  # Expected: 17

# Example 2
X2 = "abcdef"
Y2 = "pafdefycbde"
S2, R2 = 4, 2
result2 = XfromY(X2, Y2, S2, R2)
print(f"Result for Example 2: {result2}")  # Expected: 6
