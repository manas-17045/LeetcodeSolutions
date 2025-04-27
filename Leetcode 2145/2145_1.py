"""
[Leetcode 2145: Count the Hidden Sequences]
(https://leetcode.com/problems/count-the-hidden-sequences/)
"""
from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        current_relative_value = 0
        min_relative_value = 0
        max_relative_value = 0

        # Iterate through the differences to find the full range of relative values
        for diff in differences:
            current_relative_value += diff
            min_relative_value = min(min_relative_value, current_relative_value)
            max_relative_value = max(max_relative_value, current_relative_value)

        # Calculate the tightest possible bounds for the starting element (hidden[0]).
        # The start value must be high enough so that when the minimum relative value is added, it's still >= lower
        possible_min_start = lower - min_relative_value

        # The start value must be low enough so that when the maximum relative value is added, it's still <= upper
        possible_max_start = upper - max_relative_value

        # Calculate the number of possible integer values within the valid range [possible_min_start,
        # possible_max_start].
        # The count is (max - min + 1).
        count = possible_max_start - possible_min_start + 1

        # If possible_max_start < possible_min_start, the range is invalid, meaning no valid start value exists.
        # In this case, the count will be <= 0. We return max(0, count) to handle this.
        return max(0, count)