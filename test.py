def calculate_rostering_days(N, M, connections, K):
    friends = {}
    for i in range(N):
        friends[i] = set()
    for u, v in connections:
        friends[u].add(v)
        friends[v].add(u)

    rostering = N
    day = 1
    office = set(range(N))

    while rostering < K:
        day += 1
        new_office = set()
        for employee in range(N):
            friends_in_office = office & friends[employee]
            if employee in office and len(friends_in_office) == 3:
                new_office.add(employee)
            elif employee not in office and len(friends_in_office) < 3:
                new_office.add(employee)
        office = new_office
        rostering += len(office)

    return day


# # Get input from the user
# N, M = map(int, input("Enter number of employees and friendships: ").split())
# connections = []
# for _ in range(M):
#     u, v = map(int, input("Enter IDs of two friends: ").split())
#     connections.append((u, v))
# K = int(input("Enter the target rostering value: "))

# # Calculate and print the result
# days = calculate_rostering_days(N, M, connections, K)
# print(days)

N = 4  
M = 5
connections = [(1, 3), (3, 2), (0, 3), (0, 1), (2, 1)]
K = 8 


days = calculate_rostering_days(N, M, connections, K)
print(days)  # Output: 3
