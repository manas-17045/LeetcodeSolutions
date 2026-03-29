# Leetcode 3878: Count Good Subarrays
# https://leetcode.com/problems/count-good-subarrays/
# Solved on 29th of March, 2026
class Solution:
    def countGoodSubarrays(self, nums: list[int]) -> int:
        """
        Calculates the total number of good subarrays within the given list.

        :param nums: A list of integers representing the input array.
        :return: An integer representing the total count of good subarrays.
        """
        n = len(nums)
        leftBound = [0] * n
        rightBound = [0] * n

        lastPositionOfBit = [-1] * 30
        lastSeenValue = {}

        for i in range(n):
            violatingIndex = -1
            num = nums[i]

            for b in range(30):
                if (num & (1 << b)) == 0:
                    if lastPositionOfBit[b] > violatingIndex:
                        violatingIndex = lastPositionOfBit[b]

            if num in lastSeenValue:
                if lastSeenValue[num] > violatingIndex:
                    violatingIndex = lastSeenValue[num]

            leftBound[i] = violatingIndex + 1

            for b in range(30):
                if (num & (1 << b)) != 0:
                    lastPositionOfBit[b] = i

            lastSeenValue[num] = i

        nextPositionOfBit = [n] * 30

        for i in range(n - 1, -1, -1):
            violatingIndex = n
            num = nums[i]

            for b in range(30):
                if (num & (1 << b)) == 0:
                    if nextPositionOfBit[b] < violatingIndex:
                        violatingIndex = nextPositionOfBit[b]

            rightBound[i] = violatingIndex - 1

            for b in range(30):
                if (num & (1 << b)) != 0:
                    nextPositionOfBit[b] = i

        totalGoodSubarrays = 0

        for i in range(n):
            leftWays = i - leftBound[i] + 1
            rightWays = rightBound[i] - i + 1
            totalGoodSubarrays += leftWays * rightWays

        return totalGoodSubarrays