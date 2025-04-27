"""
[Leetcode 2145: Count the Hidden Sequences]
(https://leetcode.com/problems/count-the-hidden-sequences/)
"""

class Solution:
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:
        current = 0
        min_val = 0
        max_val = 0

        # Track the running sum and the min/max values encountered
        for diff in differences:
            current += diff
            min_val = min(min_val, current)
            max_val = max(max_val, current)

        # Calculate the range of our constructed sequence
        sequence_range = max_val - min_val

        # Calculate the available shifting range
        available_range = upper - lower

        # The number of possible sequences equals the number of possible shifts.
        # If we shift by 1, we get a new valid sequence, as long as we stay within bounds
        possible_shifts = available_range - sequence_range + 1

        return max(0, possible_shifts)