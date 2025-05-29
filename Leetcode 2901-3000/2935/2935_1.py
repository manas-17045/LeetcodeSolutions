# Leetcode 2935: Maximum Strong Pair XOR II
# https://leetcode.com/problems/maximum-strong-pair-xor-ii/
# Solved on 29th of May, 2025

class TrieNode:
    def __init__(self):
        self.children: dict[int, TrieNode] = {}
        self.count: int = 0


class Trie:
    def __init__(self, max_bits: int):
        self.root: TrieNode = TrieNode()
        self.max_bits = max_bits

    def add(self, num: int):
        curr = self.root
        curr.count += 1
        for i in range(self.max_bits - 1, -1, -1):
            bit = (num >> i) & 1
            if bit not in curr.children:
                curr.children[bit] = TrieNode()
            curr = curr.children[bit]
            curr.count += 1

    def remove(self, num: int):
        curr = self.root
        curr.count -= 1
        for i in range(self.max_bits - 1, -1, -1):
            bit = (num >> i) & 1
            child = curr.children[bit]
            child.count -= 1
            if child.count == 0:
                del curr.children[bit]
                return
            curr = child

    def queryMaxXor(self, num: int) -> int:
        curr = self.root

        current_max_xor = 0
        for i in range(self.max_bits - 1, -1, -1):
            bit_num = (num >> i) & 1
            desired_bit_for_x = 1 - bit_num

            if desired_bit_for_x in curr.children:
                current_max_xor |= (1 << i)
                curr = curr.children[desired_bit_for_x]
            else:
                curr = curr.children[bit_num]
        return current_max_xor


class Solution:
    def maximumStrongPairXor(self, nums: list[int]) -> int:
        """
        Finds the maximum XOR value of a "strong pair" (x, y) from the given array nums.
        A pair (x, y) is strong if |x - y| <= min(x, y).
        This is equivalent to y <= 2x if x <= y, or x <= 2y if y <= x.
        Since we sort the array and consider pairs (nums[left], nums[right]) where left <= right,
        the condition simplifies to nums[right] <= 2 * nums[left], or nums[left] >= nums[right] / 2.

        Args:
            nums: A list of integers.
        Returns:
            The maximum XOR value among all strong pairs.
        """
        nums.sort()
        MAX_BITS = 20

        trie = Trie(MAX_BITS)
        max_overall_xor = 0
        left = 0  # Left pointer of the sliding window nums[left...right]

        # Iterate 'y' (nums[right]) through the sorted array
        # This loop runs N times.
        for right in range(len(nums)):
            y = nums[right]
            trie.add(y)  # O(MAX_BITS)

            # For a pair (x,y) to be strong, if x <= y, then y <= 2x, which means x >= y/2.
            # We need x >= ceil(y/2).
            # This is the minimum value an 'x' (from nums[left...right]) can have to form a strong pair with 'y'.
            min_x_limit = (y + 1) // 2  # ceil(y/2) for positive y

            # Adjust the left end of the window:
            # Remove elements nums[left] from Trie if they are too small to satisfy x >= min_x_limit.
            # The 'left' pointer advances at most N times in total over all outer loop iterations.
            # Each trie.remove() is O(MAX_BITS). Total for this part: O(N * MAX_BITS).
            while nums[left] < min_x_limit:
                trie.remove(nums[left])
                left += 1

            # At this point, all numbers 'x_val' currently in the Trie (these are nums[k] for k in [left, right])
            # satisfy:
            #   1. x_val >= nums[left] >= min_x_limit (i.e., x_val >= y/2)
            #   2. x_val <= nums[right] = y (because nums is sorted and k <= right)
            # These two conditions ensure (x_val, y) is a strong pair.
            # Now, query the Trie for an x_val that maximizes (x_val XOR y).
            current_y_max_xor = trie.queryMaxXor(y)  # O(MAX_BITS)

            if current_y_max_xor > max_overall_xor:
                max_overall_xor = current_y_max_xor

        return max_overall_xor
