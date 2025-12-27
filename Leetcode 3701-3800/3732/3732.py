# Leetcode 3732: Maximum Product of Three Elements After One Replacement
# https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/
# Solved on 27th of December, 2025
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """
        Calculates the maximum product of three elements after one replacement.

        :param nums: A list of integers.
        :return: The maximum product of three elements after one replacement.
        """
        n = len(nums)
        nums.sort()

        relevantIndices = set()
        for i in [0, 1, 2, n - 3, n - 2, n - 1]:
            if 0 <= i < n:
                relevantIndices.add(i)

        sortedIndices = sorted(list(relevantIndices))
        maxP = -float('inf')

        removalCandidates = {0, 1, n - 2, n - 1}

        for remIdx in removalCandidates:
            if remIdx < 0 or remIdx >= n:
                continue

            pool = [i for i in sortedIndices if i != remIdx]

            for i in range(len(pool)):
                for j in range(i + 1, len(pool)):
                    pairProd = nums[pool[i]] * nums[pool[j]]
                    maxP = max(maxP, pairProd * 100000, pairProd * -100000)

        if n > 4:
            pool = [0, 1, n - 2, n - 1]
            for i in range(len(pool)):
                for j in range(i + 1, len(pool)):
                    pairProd = nums[pool[i]] * nums[pool[j]]
                    maxP = max(maxP, pairProd * 100000, pairProd * -100000)

        return maxP