# Leetcode 3806: Maximum Bitwise AND After Increment Operations
# https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/
# Solved on 28th of February, 2026
class Solution:
    def maximumAND(self, nums: list[int], k: int, m: int) -> int:
        """
        Calculates the maximum possible bitwise AND of at least m elements after
        incrementing any number of elements in nums, such that the total
        increments for any single element do not exceed k.

        :param nums: List of integers to be modified.
        :param k: Maximum allowed increment for each individual element.
        :param m: Minimum number of elements required to achieve the bitwise AND.
        :return: The maximum possible bitwise AND value.
        """
        ans = 0

        masks = [(1 << b) - 1 for b in range(35)]
        powers = [1 << b for b in range(35)]

        for bit in range(31, -1, -1):
            target = ans | powers[bit]
            targetBits = [b for b in range(31, -1, -1) if (target >> b) & 1]

            costs = []
            for x in nums:
                if (x & target) == target:
                    costs.append(0)
                    continue

                y = x
                for b in targetBits:
                    if not ((y >> b) & 1):
                        y += (powers[b] - (y & masks[b]))
                        if y - x > k:
                            y = x + k + 1
                            break

                costs.append(y - x)

            costs.sort()
            if sum(costs[:m]) <= k:
                ans = target

        return ans