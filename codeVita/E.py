def min_presses(vertices, brush_size):
    """
    Calculates the minimum number of presses needed to paint a rectilinear wall.

    Args:
      vertices: A list of tuples representing the (x, y) coordinates
                of the wall's vertices in anticlockwise order.
      brush_size: The size of the square brush.

    Returns:
      The minimum number of presses required.
    """

    area = 0
    # Calculate the area of the wall using Shoelace formula
    for i in range(len(vertices)):
        j = (i + 1) % len(vertices)
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[i][1] * vertices[j][0]
    area = abs(area) / 2

    # Calculate the number of presses needed to cover the area
    presses = area // (brush_size * brush_size)
    if area % (brush_size * brush_size) != 0:
        presses += 1

    return int(presses)


# Example usage
vertices = [
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
brush_size = 2
presses = min_presses(vertices, brush_size)
print(f"Minimum presses needed: {presses}")  # Output: 2
