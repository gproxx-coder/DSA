# https://leetcode.com/problems/couples-holding-hands/
from typing import List


def swap_couples(row: List[int]) -> int:
    ans = 0

    for i in range(0, len(row), 2):
        j = row.index(row[i] ^ 1)
        row[i + 1], row[j] = row[j], row[i + 1]
        ans += row[j] != row[i + 1]

    return ans


# couples = [0,2,1,3]  # 1
couples = [3, 2, 0, 1]  # 0

print(swap_couples(couples))
