# Leetcode 3499: Maximize Active Section with Trade I
# https://leetcode.com/problems/maximize-active-section-with-trade-i/
# Solved on 30th of October, 2025
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        """
        Calculates the maximum number of active sections (contiguous '1's) after performing at most one trade.

        Args:
            s (str): A binary string representing active ('1') and inactive ('0') sections.
        Returns:
            int: The maximum number of active sections possible after one trade.
        """
        initialOnes = s.count('1')
        t = '1' + s + '1'
        n = len(t)
        i = 0
        blocks = []

        while i < n:
            char = t[i]
            j = i
            while j < n and t[j] == char:
                j += 1
            blocks.append((char, j - i))
            i = j

        allBuyBlocks = []
        allSellBlocks = []
        allSellLengths = []

        numBlocks = len(blocks)
        if numBlocks < 3:
            return initialOnes

        for k in range(1, numBlocks - 1):
            prevChar, prevLen = blocks[k - 1]
            currChar, currLen = blocks[k]
            nextChar, nextLen = blocks[k + 1]

            if currChar == '0' and prevChar == '1' and nextChar == '1':
                allBuyBlocks.append(currLen)

            if currChar == '1' and prevChar == '0' and nextChar == '0':
                allSellBlocks.append((k, currLen))
                allSellLengths.append(currLen)

        maxInitialBuy = max(allBuyBlocks or [0])
        minInitialSell = min(allSellLengths or [float('inf')])

        res1 = initialOnes
        if maxInitialBuy > 0 and minInitialSell != float('inf'):
            res1 = initialOnes + max(0, maxInitialBuy - minInitialSell)

        maxGainCase2 = 0
        for sellIndex, sellLen in allSellBlocks:
            prevZeroLen = blocks[sellIndex - 1][1]
            nextZeroLen = blocks[sellIndex + 1][1]
            gain = prevZeroLen + nextZeroLen
            maxGainCase2 = max(maxGainCase2, gain)

        res2 = initialOnes + maxGainCase2

        return max(res1, res2)