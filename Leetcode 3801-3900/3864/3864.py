# Leetcode 3864: Minimum Cost to Partition a Binary String
# https://leetcode.com/problems/minimum-cost-to-partition-a-binary-string/
# Solved on 15th of March, 2026
class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        """
        Calculates the minimum cost to partition a binary string based on encoding and flat costs.

        :param s: The input binary string to be partitioned.
        :param encCost: The cost multiplier for encoding segments containing '1's.
        :param flatCost: The fixed cost for segments containing only '0's.
        :return: The minimum total cost to partition the string.
        """
        n = len(s)
        currLen = n
        while currLen % 2 == 0:
            currLen //= 2

        currCosts = []
        currOnes = []

        for i in range(0, n, currLen):
            ones = s[i:i+currLen].count('1')
            currOnes.append(ones)
            if ones > 0:
                currCosts.append(currLen * ones * encCost)
            else:
                currCosts.append(flatCost)

        while currLen < n:
            newLen = currLen * 2
            nextCosts = []
            nextOnes = []
            for i in range(0, len(currCosts), 2):
                ones = currOnes[i] + currOnes[i+1]
                nextOnes.append(ones)
                if ones > 0:
                    baseCost = newLen * ones * encCost
                else:
                    baseCost = flatCost

                splitCost = currCosts[i] + currCosts[i + 1]
                nextCosts.append(min(baseCost, splitCost))

            currCosts = nextCosts
            currOnes = nextOnes
            currLen = newLen

        return currCosts[0]