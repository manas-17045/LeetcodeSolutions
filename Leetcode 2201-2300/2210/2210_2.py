# Leetcode 2210: Count Hills and Valleys in an Array
# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/
# Solved on 27th of July, 2025
class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        """
        Counts the number of hills and valleys in a given array of integers.
        :param nums: A list of integers.
        :return: The total count of hills and valleys.
        """
        # Remove consecutive duplicates
        filtered = []
        for x in nums:
            if not filtered or filtered[-1] != x:
                filtered.append(x)

        # Count hills and valleys in the filtered array
        count = 0
        for i in range(1, len(filtered) - 1):
            if filtered[i] > filtered[i - 1] and filtered[i] > filtered[i + 1]:
                count += 1
            elif filtered[i] < filtered[i - 1] and filtered[i] < filtered[i + 1]:
                count += 1

        return count