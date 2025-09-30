# Leetcode 3265: Count Almost Equal Pairs I
# https://leetcode.com/problems/count-almost-equal-pairs-i/
# Solved on 30th of September, 2025
import collections


class Solution:
    def countPairs(self, nums: list[int]) -> int:
        """
        Counts the number of pairs (i, j) such that i < j and nums[i] and nums[j] are either equal or one can be obtained by swapping two digits of the other.

        Args:
            nums: A list of integers.
        Returns:
            The total number of such pairs.
        """
        swappedVersionsCache = {}

        def getSwappedVersions(n: int) -> set:

            if n in swappedVersionsCache:
                return swappedVersionsCache[n]

            s = str(n)
            numDigits = len(s)
            result = set()
            sAsList = list(s)

            if numDigits > 1:
                for i in range(numDigits):
                    for j in range(i + 1, numDigits):
                        sAsList[i], sAsList[j] = sAsList[j], sAsList[i]
                        swappedNumStr = "".join(sAsList)
                        result.add(int(swappedNumStr))
                        sAsList[i], sAsList[j] = sAsList[j], sAsList[i]

            swappedVersionsCache[n] = result
            return result

        numCounts = collections.Counter(nums)
        uniqueNums = list(numCounts.keys())
        numUnique = len(uniqueNums)
        pairCount = 0

        for num in uniqueNums:
            count = numCounts[num]
            if count > 1:
                pairCount += count * (count - 1) // 2

        for i in range(numUnique):
            for j in range(i + 1, numUnique):
                num1 = uniqueNums[i]
                num2 = uniqueNums[j]

                if num2 in getSwappedVersions(num1) or num1 in getSwappedVersions(num2):
                    pairCount += numCounts[num1] * numCounts[num2]

        return pairCount