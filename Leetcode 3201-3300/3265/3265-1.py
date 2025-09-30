# Leetcode 3265: Count Almost Equal Pairs I
# https://leetcode.com/problems/count-almost-equal-pairs-i/
# Solved on 30th of September, 2025
from collections import defaultdict


class Solution:
    def countPairs(self, nums: list[int]) -> int:
        """
        Counts the number of "almost equal" pairs in the given list of integers.
        :param nums: A list of integers.
        :return: The total count of almost equal pairs.
        """
        def getVariations(s):
            variations = {s}
            n = len(s)

            for i in range(n):
                for j in range(i + 1, n):
                    swapped = list(s)
                    swapped[i], swapped[j] = swapped[j], swapped[i]
                    variations.add(''.join(swapped))

            return variations

        maxLen = len(str(max(nums)))
        count = 0
        seen = defaultdict(int)

        for num in nums:
            paddedNum = str(num).zfill(maxLen)
            variations = getVariations(paddedNum)

            for var in variations:
                if var in seen:
                    count += seen[var]

            seen[paddedNum] += 1

        return count