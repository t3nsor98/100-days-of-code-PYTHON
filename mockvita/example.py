def conflict_free_team(n, conflicts):
    team = set()
    for person in range(1, n + 1):
        if all(
            conflicting_person not in team
            for conflicting_person in conflicts.get(person, [])
        ):
            team.add(person)
    return sorted(team)


def get_user_input():
    n = int(input("Enter the number of people (n): "))
    m = int(input("Enter the number of conflicts (m): "))

    conflicts = {}
    print("Enter each conflict as 'a b' where a and b are conflicting people:")
    for _ in range(m):
        a, b = map(int, input().split())
        conflicts.setdefault(a, []).append(b)
        conflicts.setdefault(b, []).append(a)

    return n, conflicts


def main():
    n, conflicts = get_user_input()
    team = conflict_free_team(n, conflicts)
    print(f"\nSize of the conflict-free team: {len(team)}")
    print(f"Members of the conflict-free team: {' '.join(map(str, team))}")


if __name__ == "__main__":
    main()
