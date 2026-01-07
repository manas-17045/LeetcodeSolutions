# Leetcode 2772: Apply Operations to Make All Array Elements Equal to Zero
# https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/
# Solved on 7th of January, 2026
class Solution:
    def checkArray(self, nums: list[int], k: int) -> int:
        """
        Checks if all elements in the array can be made zero by applying a specific operation.

        The operation involves choosing an index `i` and subtracting 1 from `nums[i]`, `nums[i+1]`, ..., `nums[i+k-1]`.

        :param nums: A list of integers representing the array.
        :param k: An integer representing the length of the subarray to apply the operation on.
        :return: True if all elements can be made zero, False otherwise.
        """
        n = len(nums)
        currentSubtract = 0
        for i in range(n):
            if i >= k:
                currentSubtract -= nums[i - k]

            if nums[i] < currentSubtract:
                return False

            needed = nums[i] - currentSubtract

            if needed > 0:
                if i + k > n:
                    return False
                currentSubtract += needed

            nums[i] = needed

        return True