# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/


def min_cost(colors, needed_time):
    min_sum = 0
    for idx in range(0, len(colors) - 1):
        if colors[idx] == colors[idx + 1]:
            if needed_time[idx] < needed_time[idx + 1]:
                min_sum += needed_time[idx]
            else:
                min_sum += needed_time[idx+1]
                needed_time[idx + 1] = needed_time[idx]
    return min_sum


# colors = "abaac"
# needed_time = [1, 2, 3, 4, 5]

# colors = "aabaa"
# needed_time = [1, 2, 3, 4, 1]

colors = "aaabbbabbbb"
needed_time = [3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1]

print(min_cost(colors, needed_time))
