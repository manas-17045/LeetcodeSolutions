# Leetcode 1521: Find a Value of a Mysterious Function Closest to Target
# https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/
# Solved on 18th of July, 2025
class Solution:
    def closestToTarget(self, arr: list[int], target: int) -> int:
        """
        Finds the minimum absolute difference between `target` and any bitwise AND subarray result.
        :param arr: A list of integers.
        :param target: The target integer.
        :return: The minimum absolute difference.
        """
        rolling_set = set()
        # Initialize answer to a large value
        best = float('inf')

        for x in arr:
            # Start a new set for subarrays ending at current x
            new_set = {x}
            for prev_and in rolling_set:
                new_set.add(prev_and & x)

            rolling_set = new_set

            # Update best difference from target
            for v in rolling_set:
                diff = abs(v - target)
                if diff < best:
                    best = diff
                    # Early exit if perfect match found
                    if best == 0:
                        return 0

        return best