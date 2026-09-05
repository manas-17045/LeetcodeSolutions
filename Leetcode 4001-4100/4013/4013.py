# Leetcode 4013: Count Subarrays With Even Odd Ratio II
# https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii/
# Solved on 5th of September, 2026
class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        """
        Counts the number of valid subarrays where the ratio of even to odd elements is at most a / b.

        Args:
            nums (list[int]): The input array of integers.
            a (int): The numerator of the maximum allowed ratio.
            b (int): The denominator of the maximum allowed ratio.

        Returns:
            int: The total number of valid subarrays.
        """
        prefixSums = [0]
        currentSum = 0

        for num in nums:
            if num % 2 == 0:
                currentSum += b
            else:
                currentSum -= a
            prefixSums.append(currentSum)

        sortedUniqueSums = sorted(list(set(prefixSums)))
        rankMap = {val: i + 1 for i, val in enumerate(sortedUniqueSums)}
        maxRank = len(sortedUniqueSums)
        fenwickTree = [0] * (maxRank + 1)

        def updateTree(index: int, value: int) -> None:
            while index <= maxRank:
                fenwickTree[index] += value
                index += index & (-index)

        def queryPrefix(index: int) -> int:
            total = 0
            while index > 0:
                total += fenwickTree[index]
                index -= index & (-index)
            return total

        validSubarraysCount = 0
        elementsSeen = 0

        for prefix in prefixSums:
            currentRank = rankMap[prefix]
            countStrictlyLess = queryPrefix(currentRank - 1)
            validSubarraysCount += elementsSeen - countStrictlyLess
            
            updateTree(currentRank, 1)
            elementsSeen += 1

        return validSubarraysCount