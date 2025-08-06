# Leetcode 3479: Fruits Into Baskets III
# https://leetcode.com/problems/fruits-into-baskets-iii/
# Solved on 6th of August, 2025
class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        """
        Calculates the number of fruits that cannot be placed in any of the baskets.

        Args:
            fruits: A list of integers representing the sizes of the fruits.
            baskets: A list of integers representing the capacities of the baskets.

        Returns:
            The total number of fruits that could not be placed in any of the baskets.
        """
        n = len(baskets)
        # Build segment tree of size = next power of two >= n
        size = 1
        while size < n:
            size <<= 1
        seg = [0] * (2 * size)
        # Initialize leaves
        for i, cap in enumerate(baskets):
            seg[size + i] = cap
        # Build internal nodes
        for i in range(size - 1, 0, -1):
            seg[i] = max(seg[2 * i], seg[2 * i + 1])

        def place(f: int) -> bool:
            if seg[1] < f:
                # No basket can fit this fruit
                return False
            
            # Descend to find leftmost leaf with cap >= f.
            idx = 1
            while idx <  size:
                # If left child can accomodate, go left; otherwise, go right
                if seg[2 * idx] >= f:
                    idx = 2 * idx
                else:
                    idx = 2 * idx + 1
            
            # idx is now a leaf in [sizze...size+n-1]
            pos = idx - size
            # Mark basket used by zeroing capacity
            seg[idx] = 0
            # Update ancestors
            idx //= 2
            while idx:
                seg[idx] = max(seg[2 * idx], seg[2 * idx + 1])
                idx //= 2
            return True
        
        unplaced = 0
        for f in fruits:
            if not place(f):
                unplaced += 1
        
        return unplaced