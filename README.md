# Video Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

We are interested in analyzing how a video gets shared with group of friends.

We will work with a dictionary that shows us who is friends with whom. In this dictionary, a person will be the key, and the value will be a `set` containing all the people they are friends with. For example:

```py
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
```

In this example, we see that Sebastian has three friends: Kevin, Lewis, and Fernando. Conversely, Lewis only has a single friend: Sebastian.

We choose a random person to show a viral video to, and after watching it they share it with all their friends who share it with all their friends and so on. For example, if we showed Lewis our video, it would travel like this:

- Lewis watches the video
- Lewis shares the video with Sebastian
- Sebastian shares the video with Kevin and Fernando
- Fernando shares the video with Max

In this scenario, five people will end up seeing the video (Lewis, Sebastian, Kevin, Fernando, and Max).

Write a function that accepts a friend dictionary and an initial person to show it to. The function should return the overall number of people that end up watching to movie as a result.

Neither the dictionary nor the sets inside should be modified.

## Examples

For the following friend data:

```py
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
```

The following table shows a selection of people, and the group size that would result from showing the video to them:

| Person    | Group Size |
| --------- | ---------- |
| Sebastian | 5          |
| Max       | 2          |
| Lewis     | 5          |
| Yuki      | 2          |
| Carlos    | 3          |
| Charles   | 3          |

## Notes for the Interviewer

### Clarifying Questions

#### Q: Are friendships always bidirectional?

A: Yes. If person A is friends with person B, you are guaranteed that person B is also friends with person A. It will always go in both directions.

#### Q: Should I include the input person in the count?

A: Yes.

#### Q: Can someone show up in the values but not in the keys?

A: No. You are guaranteed that if a person shows up in the values then they will have a corresponding key in the dictionary.

#### Q: What if I am passed a person who is not in the dictionary?

A: You are guaranteed the input person will be a key in the dictionary.

#### Q: What should I do if there's invalid data?

A: You can assume the data will be valid.

#### Q: Can I mutate the input?

A: No.

### Hints

- If your candidate struggles with an initial algorithm, ask them what type of search algorithm would be helpful here. Either BFS or DFS can work! Have them talk through what needs to happen at each step of the search. Have them talk through an example starting with Sebastian, and have them describe which positions would be visited in what order.

- Encourage your candidate to print the person at each step of the search if they are not passing the test cases and are unsure why. This can help debug the path that the search takes (and can be especially helpful for debugging infinite loops).

## Optional Bonus At-Home Challenges

To be attempted after completing the interview.

- What are the time/space complexities of the sample solution?

- If you wrote a solution that used DFS, try writing a solution that uses BFS or vice versa.

- If you wrote a solution that used recursion, try writing a solution that uses iteration or vice versa.

### Extra Hard

- Suppose that instead of a person being guaranteed to send a video to a friend, they instead only have a 1 in 3 chance to send it to each person. Write a function that accepts a dictionary and a start person and returns the expected (average) number of people it will be sent to. Trying solving this in two ways: one by applying probability theory and one by using Monte Carlo sampling. Research either as necessary to achieve this.

- Solve the previous probability problem, but this time return an EXACT result - no rounding error from floats or decimals allowed. Hint: research the built-in Python `fractions` module.
