# Leetcode 3936: Minimum Swaps to Move Zeros to End
# https://leetcode.com/problems/minimum-swaps-to-move-zeros-to-end/
# Solved on 4th of June, 2026
class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of swaps required to move all zeros to the end of the array.

        :param nums: A list of integers containing zeros and non-zero elements.
        :return: The minimum number of swaps needed to group all zeros at the end.
        """
        zeroCount = nums.count(0)
        prefixLength = len(nums) - zeroCount

        misplacedZeros = 0
        for i in range(prefixLength):
            if nums[i] == 0:
                misplacedZeros += 1

        return misplacedZeros