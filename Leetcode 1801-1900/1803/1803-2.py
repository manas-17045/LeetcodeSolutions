# Leetcode 1803: Count Pairs With XOR in a Range
# https://leetcode.com/problems/count-pairs-with-xor-in-a-range/
# Solved on 23rd of September, 2025
class TrieNode:
    __slots__ = ("children", "count")
    def __init__(self):
        self.children = [None, None]
        self.count = 0

class Solution:
    def countPairs(self, nums: list[int], low: int, high: int) -> int:
        """
        Counts the number of pairs (i, j) such that i < j and low <= (nums[i] XOR nums[j]) <= high.
        :param nums: A list of integers.
        :param low: The lower bound for the XOR sum.
        :param high: The upper bound for the XOR sum.
        :return: The number of pairs satisfying the conditions.
        """
        if not nums:
            return 0

        # Determine number of bits needed (cover both nums and high)
        max_val = max(max(nums), high)
        maxBit = max_val.bit_length()
        if maxBit == 0:
            maxBit = 1
        maxBit -= 1

        root = TrieNode()

        def insert(x: int) -> None:
            node = root
            node.count += 1
            for k in range(maxBit, -1, -1):
                b = (x >> k) & 1
                if node.children[b] is None:
                    node.children[b] = TrieNode()
                node = node.children[b]
                node.count += 1

        def count_leq(x: int, limit: int) -> int:
            if limit < 0:
                return 0

            node = root
            res = 0
            for k in range(maxBit, -1, -1):
                if node is None:
                    break
                xb = (x >> k) & 1
                lb = (limit >> k) & 1
                if lb == 1:
                    child = node.children[xb]
                    if child:
                        res += child.count
                    node = node.children[1 - xb]
                else:
                    node = node.children[xb]

            if node:
                res += node.count
            return res

        ans = 0
        # Iterate counting pairs where previous numbers are considered
        for x in nums:
            cnt_high = count_leq(x, high)
            cnt_low_minus_1 = count_leq(x, (low - 1))
            ans += (cnt_high - cnt_low_minus_1)
            insert(x)

        return ans