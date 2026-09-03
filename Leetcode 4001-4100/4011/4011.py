# Leetcode 4011: Count Subarrays With Even Odd Ratio I
# https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-i/
# Solved on 3rd of September, 2026
class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        """
        Counts the number of subarrays with an even-to-odd ratio at most a / b and at least one odd element.

        Parameters:
            nums (list[int]): The array of integers to evaluate.
            a (int): The numerator of the maximum allowable ratio.
            b (int): The denominator of the maximum allowable ratio.

        Returns:
            int: The total count of valid subarrays.
        """
        validSubarrays = 0
        totalLength = len(nums)

        for startIndex in range(totalLength):
            evenCount = 0
            oddCount = 0

            for endIndex in range(startIndex, totalLength):
                if nums[endIndex] % 2 == 0:
                    evenCount += 1
                else:
                    oddCount += 1

                if oddCount > 0 and (evenCount * b) <= (oddCount * a):
                    validSubarrays += 1

        return validSubarrays