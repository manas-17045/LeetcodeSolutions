# Leetcode 1803: Count Pairs With XOR in a Range
# https://leetcode.com/problems/count-pairs-with-xor-in-a-range/
# Solved on 23rd of September, 2025
class Solution:
    def countPairs(self, nums: list[int], low: int, high: int) -> int:
        """
        Counts the number of pairs (i, j) such that low <= (nums[i] XOR nums[j]) <= high.

        Args:
            nums: A list of integers.
            low: The lower bound for the XOR sum.
            high: The upper bound for the XOR sum.

        Returns: The number of pairs (i, j) satisfying the condition.
        """

        class TrieNode:
            def __init__(self):
                self.children = {}
                self.count = 0

        class Trie:
            def __init__(self):
                self.root = TrieNode()
                self.maxBit = 14

            def insert(self, number):
                node = self.root
                for i in range(self.maxBit, -1, -1):
                    bit = (number >> i) & 1
                    if bit not in node.children:
                        node.children[bit] = TrieNode()
                    node = node.children[bit]
                    node.count += 1

            def queryCountSmaller(self, number, limit):
                node = self.root
                count = 0
                for i in range(self.maxBit, -1, -1):
                    if not node:
                        break

                    limitBit = (limit >> i) & 1
                    numBit = (number >> i) & 1

                    if limitBit == 1:
                        if numBit in node.children:
                            count += node.children[numBit].count
                        node = node.children.get(1 - numBit)
                    else:
                        node = node.children.get(numBit)
                return count

        trie = Trie()
        totalPairs = 0

        for num in nums:
            countHigh = trie.queryCountSmaller(num, high + 1)
            countLow = trie.queryCountSmaller(num, low)
            totalPairs += countHigh - countLow
            trie.insert(num)

        return totalPairs