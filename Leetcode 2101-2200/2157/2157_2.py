# Leetcode 2157: Groups of Strings
# https://leetcode.com/problems/groups-of-strings/
# Solved on 9th of July, 2025
class DSU:
    def __init__(self, n: int):
        self.p = list(range(n))
        self.sz = [1] * n

    def find(self, x: int) -> int:
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, x: int, y: int) -> None:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        # Union by size
        if self.sz[rx] < self.sz[ry]:
            rx, ry = ry, rx
        self.p[ry] = rx
        self.sz[rx] += self.sz[ry]

class Solution:
    def groupStrings(self, words: list[str]) -> list[int]:
        """
        Groups strings based on specific transformation rules and returns the number of groups
        and the size of the largest group.

        Two strings are in the same group if one can be transformed into the other by a sequence
        of operations:
        1. Adding a character not present in the string.
        2. Deleting a character present in the string.
        3. Replacing a character with another character.

        Args:
            words: A list of strings.
        Returns:
            A list containing two integers: [number_of_groups, size_of_largest_group].
        """
        n = len(words)
        # Build bitmasks
        masks = [0] * n
        for i, w in enumerate(words):
            bitmask = 0
            for ch in w:
                bitmask |= 1 << (ord(ch) - ord('a'))
            masks[i] = bitmask

        dsu = DSU(n)
        mask_to_index = {}

        # Union duplicates (same mask)
        for i, m in enumerate(masks):
            if m in mask_to_index:
                dsu.union(i, mask_to_index[m])
            else:
                mask_to_index[m] = i

        # For each word, try all +1/-1-bit flips (add/delete) and all replace patterns
        ALL_BITS = 26
        for i, m in enumerate(masks):
            for b in range(ALL_BITS):
                m2 = m ^ (1 << b)
                j = mask_to_index.get(m2)
                if j is not None:
                    dsu.union(i, j)

            mbits = m
            b1 = mbits
            while b1:
                lsb = b1 & -b1
                b1 ^= lsb
                idx1 = (lsb.bit_length() - 1)
                # Iterate over zero bits
                zero_mask = (~m) & ((1 << ALL_BITS) - 1)
                b2 = zero_mask
                while b2:
                    lsb2 = b2 & -b2
                    b2 ^= lsb2
                    idx2 = (lsb2.bit_length() - 1)
                    m3 = (m ^ (1 << idx1)) | (1 << idx2)
                    j = mask_to_index.get(m3)
                    if j is not None:
                        dsu.union(i, j)

        # Collect group sizes
        group_count = 0
        largest = 0
        # Use a simple frequency map of root → size
        freq = {}
        for i in range(n):
            r = dsu.find(i)
            freq[r] = freq.get(r, 0) + 1
        for size in freq.values():
            group_count += 1
            if size > largest:
                largest = size

        return [group_count, largest]