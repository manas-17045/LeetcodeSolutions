# Leetcode 3934: Smallest Unique Subarray
# https://leetcode.com/problems/smallest-unique-subarray/
# Solved on 2nd of June, 2026
class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        """
        Finds the length of the smallest subarray that appears exactly once in the given list.

        Args:
            nums (list[int]): The input list of integers.
        Returns:
            int: The length of the shortest unique subarray.
        """
        leftBound = 1
        rightBound = len(nums)
        minUniqueLength = len(nums)
        baseVal = 100003
        modVal = (1 << 61) - 1

        while leftBound <= rightBound:
            midVal = (leftBound + rightBound) // 2
            currentHash = 0
            powerVal = 1

            for i in range(midVal):
                currentHash = (currentHash * baseVal + nums[i]) % modVal
                if i > 0:
                    powerVal = (powerVal * baseVal) % modVal

            hashCounts = {}
            hashCounts[currentHash] = 1

            for i in range(midVal, len(nums)):
                currentHash = (currentHash - nums[i - midVal] * powerVal) % modVal
                currentHash = (currentHash * baseVal + nums[i]) % modVal

                if currentHash in hashCounts:
                    hashCounts[currentHash] += 1
                else:
                    hashCounts[currentHash] = 1

            foundUnique = False
            for countVal in hashCounts.values():
                if countVal == 1:
                    foundUnique = True
                    break

            if foundUnique:
                minUniqueLength = midVal
                rightBound = midVal - 1
            else:
                leftBound = midVal + 1

        return minUniqueLength