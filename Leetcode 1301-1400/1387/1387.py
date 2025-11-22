# Leetcode 1387: Sort Integers by The Power Value
# https://leetcode.com/problems/sort-integers-by-the-power-value/
# Solved on 22nd of November, 2025
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        """
        Given three integers lo, hi and k. The task is to sort all integers in the interval [lo, hi]
        by their power value in ascending order. If two or more integers have the same power value,
        sort them in ascending order.

        Args:
            lo (int): The lower bound of the range.
            hi (int): The upper bound of the range.
            k (int): The k-th element to return after sorting.

        Returns:
            int: The k-th integer in the range [lo, hi] sorted by its power value.
                 If two or more integers have the same power value, they are sorted
                 in ascending order.
        """
        powerCache = {1: 0}

        def getPower(num):
            if num in powerCache:
                return powerCache[num]

            if num % 2 == 0:
                steps = 1 + getPower(num // 2)
            else:
                steps = 1 + getPower(3 * num + 1)

            powerCache[num] = steps
            return steps

        valueList = []
        for x in range(lo, hi + 1):
            valueList.append((getPower(x), x))

        valueList.sort()

        return valueList[k - 1][1]