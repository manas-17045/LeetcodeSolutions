# Leetcode 3224: Minimum Array Changes to Make Differences Equal
# https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/
# Solved on 24th of November, 2025
class Solution:
    def minChanges(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum number of changes required to make the differences
        between symmetric pairs of elements in the array equal.

        Args:
            nums: A list of integers.
            k: An integer representing the maximum possible value for an element.

        Returns:
            The minimum number of changes required.
        """
        n = len(nums)
        diffTracker = [0] * (k + 2)
        halfN = n // 2

        for i in range(halfN):
            num1 = nums[i]
            num2 = nums[n - 1 - i]
            currentDiff = abs(num1 - num2)
            maxOneChange = max(num1, num2, k - num1, k - num2)

            diffTracker[0] += 1
            diffTracker[currentDiff] -= 1
            diffTracker[currentDiff + 1] += 1
            diffTracker[maxOneChange + 1] += 1

        minOps = n
        currentOps = 0

        for i in range(k + 1):
            currentOps += diffTracker[i]
            if currentOps < minOps:
                minOps = currentOps

        return minOps