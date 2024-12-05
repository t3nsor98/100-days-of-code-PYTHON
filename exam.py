from collections import defaultdict


def days_to_reach_rostering_value(N, M, friendships, K):
    # Create adjacency list for friendships
    graph = defaultdict(list)
    for a, b in friendships:
        graph[a].append(b)
        graph[b].append(a)

    # Initialize attendance
    attendance = [1] * N  # 1 means WFO, 0 means WFH
    rostering_value = N  # Day 1 all are WFO
    cumulative_value = rostering_value
    days = 1

    while cumulative_value < K:
        new_attendance = attendance[:]
        for i in range(N):
            friends_in_office = sum(attendance[friend] for friend in graph[i])
            if attendance[i] == 1:  # Currently WFO
                new_attendance[i] = 1 if friends_in_office == 3 else 0
            else:  # Currently WFH
                new_attendance[i] = 1 if friends_in_office < 3 else 0

        attendance = new_attendance
        rostering_value = sum(attendance)
        cumulative_value += rostering_value
        days += 1

    return days


# Input
input_data = """
4 5
1 3
3 2
0 3
0 1
2 1
8
"""
lines = input_data.strip().split("\n")
N, M = map(int, lines[0].split())
friendships = [tuple(map(int, line.split())) for line in lines[1 : M + 1]]
K = int(lines[M + 1])

# Output
result = days_to_reach_rostering_value(N, M, friendships, K)
print(result)
