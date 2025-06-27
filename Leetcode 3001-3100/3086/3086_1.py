# Leetcode 3086: Minimum Moves to Pick K Ones
# https://leetcode.com/problems/minimum-moves-to-pick-k-ones/
# Solved on 27th of June, 2025
class Solution:
    def minimumMoves(self, nums: list[int], k: int, maxChanges: int) -> int:
        """
        Calculates the minimum moves to achieve k ones, given the ability to change
        up to maxChanges zeros to ones.

        Args:
            nums: A list of integers (0s and 1s).
            k: The target number of ones.
            maxChanges: The maximum number of zeros that can be changed to ones.

        Returns:
            The minimum number of moves required.
        """
        oneIndices = []
        for i, num in enumerate(nums):
            if num == 1:
                oneIndices.append(i)

        if k == 0:
            return 0

        prefix = [0]
        for index in oneIndices:
            prefix.append(prefix[-1] + index)

        ans = float('inf')

        numOfIndicesWithOneDistance = 3

        minOnesByTwo = max(0, (k - maxChanges))

        maxOnesByTwo = min(k, len(oneIndices), (minOnesByTwo + numOfIndicesWithOneDistance))

        for onesByTwo in range(minOnesByTwo, (maxOnesByTwo + 1)):
            if onesByTwo == 0:
                if k <= maxChanges:
                    ans = min(ans, k * 2)
                continue

            cost1 = (k - onesByTwo) * 2

            for l in range(len(oneIndices) - onesByTwo + 1):
                r = l + onesByTwo

                mid1 = (l + r) // 2
                mid2 = (l + r + 1) // 2

                cost2 = (prefix[r] - prefix[mid2]) - (prefix[mid1] - prefix[l])

                ans = min(ans, (cost1 + cost2))

        return int(ans)