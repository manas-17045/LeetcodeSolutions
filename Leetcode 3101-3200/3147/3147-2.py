# Leetcode 3147: Taking Maximum Energy from the Mystic Dungeon
# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/
# Solved on 10th of October, 2025
class Solution:
    def maximumEnergy(self, energy: list[int], k: int) -> int:
        """
        Calculates the maximum energy that can be obtained.

        Args:
            energy (list[int]): A list of integers representing energy values.
            k (int): An integer representing the jump step.
        Returns:
            int: The maximum energy that can be obtained.
        """
        n = len(energy)
        if n == 0:
            return 0

        # Sufficiently small initial value
        best = -10**18

        # For each residue class modulo k
        for r in range(k):
            # Find the last index on this residue class
            if r >= n:
                break

            last = r + ((n - 1 - r) // k) * k

            curr = 0
            max_suffix = -10**18
            i = last

            # Iterate backwards over the subsequence to compute suffix sums
            while i >= r:
                curr += energy[i]
                if curr > max_suffix:
                    max_suffix = curr
                i -= 1

            if max_suffix > best:
                best = max_suffix

        return best