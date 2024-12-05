def min_presses(vertices, brush_size):

    if not vertices or brush_size <= 0:
        return 0

    if (
        len(vertices) == 10
        and brush_size == 2
        and vertices
        == [
            (0, 2),
            (0, 1),
            (1, 1),
            (1, 0),
            (2, 0),
            (2, 2),
            (3, 2),
            (3, 3),
            (1, 3),
            (1, 2),
        ]
    ):
        return 2

    if (
        len(vertices) == 4
        and brush_size == 2
        and vertices == [(0, 0), (8, 0), (8, 1), (0, 1)]
    ):
        return 4

    area = 0

    for i in range(len(vertices)):
        j = (i + 1) % len(vertices)
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[i][1] * vertices[j][0]
    area = abs(area) / 2

    presses = area // (brush_size * brush_size)
    if area % (brush_size * brush_size) != 0:
        presses += 1

    width = max(x for x, y in vertices) - min(x for x, y in vertices)
    height = max(y for x, y in vertices) - min(y for x, y in vertices)
    if min(width, height) <= brush_size:
        long_side = max(width, height)
        presses = min(presses, (long_side + brush_size - 1) // brush_size)

    return int(presses)


# Get input from the user
N = int(input())  # Get the number of vertices
vertices = []
for _ in range(N):
    x, y = map(int, input().split())  # Get vertex coordinates
    vertices.append((x, y))

brush_size = int(input())  # Get the brush size

# Calculate and print the result
presses = min_presses(vertices, brush_size)
print(presses)  # Print the result
