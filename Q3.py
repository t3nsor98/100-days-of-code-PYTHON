def buzz_day_sale(N, ids, costs, A):
    max_free_items = 0
    max_free_worth = 0

    for i in range(N):
        # Try buying each item
        cost = costs[i]
        free_items = 0
        free_worth = 0
        affordable_quantity = A // cost

        # Check if Veda can afford at least one of this item
        if affordable_quantity > 0:
            for j in range(N):
                # Check for free items (factors of the purchased item's ID)
                if ids[i] != ids[j] and ids[i] % ids[j] == 0:
                    free_items += affordable_quantity  # Add quantity for each free item
                    free_worth += (
                        costs[j] * affordable_quantity
                    )  # Add worth for each free item

            # Update maximums if this purchase yields better results
            if free_items > max_free_items or (
                free_items == max_free_items and free_worth > max_free_worth
            ):
                max_free_items = free_items
                max_free_worth = free_worth

    return max_free_items, max_free_worth


# Get inputs
# N = int(input())
# ids = list(map(int, input().split()))
# costs = list(map(int, input().split()))
# A = int(input())

N = 5
ids = [11, 24, 3, 12, 7]
costs = [7, 11, 15, 9, 4]  
A = 17  


max_free_items, max_free_worth = buzz_day_sale(N, ids, costs, A)
print(max_free_items, max_free_worth)
