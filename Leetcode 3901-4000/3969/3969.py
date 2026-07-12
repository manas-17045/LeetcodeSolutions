# Leetcode 3969: Valid Subarrays With Matching Sum Digits I
# https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-i/
# Solved on 12th of July, 2026
class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        """
        Counts the number of valid subarrays.
        
        @param nums The input array.
        @param x The target sum digit.
        @return The number of valid subarrays.
        """
        validCount = 0
        arrayLength = len(nums)

        for startIndex in range(arrayLength):
            runningSum = 0

            for endIndex in range(startIndex, arrayLength):
                runningSum += nums[endIndex]

                if runningSum % 10 == x:
                    currentSum = runningSum

                    while currentSum >= 10:
                        currentSum //= 10

                    if currentSum == x:
                        validCount += 1

        return validCount