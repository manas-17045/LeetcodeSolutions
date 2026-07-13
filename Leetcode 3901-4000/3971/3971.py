# Leetcode 3971: Maximum Total Value
# https://leetcode.com/problems/maximum-total-value/
# Solved on 13th of July, 2026
class Solution:
    def maxTotalValue(self, value: list[int], decay: list[int], m: int) -> int:
        """
        Calculates the maximum total value that can be obtained by selecting m items
        from n items, each with a specific value and decay rate

        :param value: values of the items
        :param decay: decay rates of the items
        :param m: number of items to take
        :return: maximum total value
        """
        modVal = 1000000007
        left = 1
        right = max(value)
        minGain = 0

        while left <= right:
            mid = (left + right) // 2
            totalCount = 0
            for val, dec in zip(value, decay):
                if val >= mid:
                    totalCount += (val - mid) // dec + 1

            if totalCount >= m:
                minGain = mid
                left = mid + 1
            else:
                right = mid - 1

        totalSum = 0
        itemsTaken = 0

        for val, dec in zip(value, decay):
            if val >= minGain + 1:
                count = (val - (minGain + 1)) // dec + 1
                totalSum += count * (2 * val - (count - 1) * dec) // 2
                itemsTaken += count

        if minGain > 0:
            totalSum += (m - itemsTaken) * minGain

        return totalSum % modVal