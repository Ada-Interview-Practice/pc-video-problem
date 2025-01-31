def group_size(friend_data, start):
    # Your solution here!
    pass


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
