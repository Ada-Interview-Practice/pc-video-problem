def group_size(friend_data, start):
    # Will hold already visited friends
    visited = set()

    # Recursive helper to count from a starting person
    def count(start):
        # Do not count a person if they've already been visited
        if start in visited:
            return 0

        # Add the person to the visited set
        visited.add(start)

        # Count the current person
        total = 1

        # Recursively call and sum from each friend
        for friend in friend_data[start]:
            total += count(friend)

        return total

    # Call helper from input person
    return count(start)


friend_data = {
    "Sebastian": {"Kevin", "Lewis", "Fernando"},
    "Max": {"Fernando"},
    "Lewis": {"Sebastian"},
    "Yuki": {"Pierre"},
    "Pierre": {"Yuki"},
    "Fernando": {"Sebastian", "Max"},
    "Carlos": {"Charles", "Lando"},
    "Lando": {"Carlos"},
    "Charles": {"Carlos"},
    "Kevin": {"Sebastian"},
}

assert group_size(friend_data, "Yuki") == 2
assert group_size(friend_data, "Carlos") == 3
assert group_size(friend_data, "Charles") == 3
assert group_size(friend_data, "Lewis") == 5
assert group_size(friend_data, "Max") == 5
assert group_size(friend_data, "Sebastian") == 5

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
