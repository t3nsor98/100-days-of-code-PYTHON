def calculate_office_days(
    total_employees, num_friendships, friendships, target_employees
):
    """
    Calculates the number of days needed to have a certain number of employees
    rostered in the office, based on friendship rules.

    Args:
      total_employees: The total number of employees.
      num_friendships: The number of friendship friendships.
      friendships: A list of tuples representing friendships between employees.
      target_employees: The desired number of employees to be rostered.

    Returns:
      The number of days required to reach the target rostering.
    """

    # Create a dictionary to store each employee's friends
    employee_friends = {}
    for employee_id in range(total_employees):
        employee_friends[employee_id] = (
            set()
        )  # Each employee starts with no friends in the office

    # Populate the dictionary with the given friendships
    for employee1, employee2 in friendships:
        employee_friends[employee1].add(employee2)
        employee_friends[employee2].add(employee1)

    # Initialize variables to track rostering progress
    current_rostering = (
        total_employees  # Start with all employees in the office on day 1
    )
    day_count = 1
    employees_in_office = set(
        range(total_employees)
    )  # Initially, all employees are in the office

    # Keep simulating days until the target rostering is reached
    while current_rostering < target_employees:
        day_count += 1
        new_employees_in_office = set()

        # Check each employee's rostering status for the next day
        for employee_id in range(total_employees):
            # Find the employee's friends who are currently in the office
            friends_at_work = employees_in_office & employee_friends[employee_id]

            # Apply the rostering rules
            if employee_id in employees_in_office and len(friends_at_work) == 3:
                new_employees_in_office.add(employee_id)  # Employee stays in the office
            elif employee_id not in employees_in_office and len(friends_at_work) < 3:
                new_employees_in_office.add(employee_id)  # Employee comes to the office

        # Update the set of employees in the office for the next day
        employees_in_office = new_employees_in_office
        current_rostering += len(employees_in_office)

    return day_count  # Return the total number of days taken


# Get input from the user
total_employees, num_friendships = map(
    int, input("Enter number of employees and friendships: ").split()
)
friendships = []
for friendship in range(num_friendships):
    u, v = map(int, input("Enter IDs of two friends: ").split())
    friendships.append((u, v))
target_employees = int(input("Enter the target rostering value: "))

days_needed = calculate_office_days(
    total_employees, num_friendships, friendships, target_employees
)
print(days_needed) 
