# Leetcode 1718: Construct the Lexicographically Largest Valid Sequence
# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        """
        Constructs the lexicographically largest valid sequence given an integer n.

        A valid sequence is a sequence of length 2n - 1 containing integers from 1 to n,
        where each integer i (1 < i <= n) appears exactly twice, and the distance between
        the two occurrences of i is exactly i. The integer 1 appears only once.

        Args:
            n: An integer representing the largest number in the sequence.

        Returns:
            A list representing the lexicographically largest valid sequence.
        """
        length = 2 * n - 1
        seq = [0] * length
        used = [False] * (n + 1)

        def backtrack(pos: int) -> bool:
            # Skip filled positions
            while pos < length and seq[pos] != 0:
                pos += 1
            # If we've filled everything, we're done
            if pos == length:
                return True

            # Try placing each number from n down to 2
            for num in range(n, 1, -1):
                if not used[num]:
                    j = pos + num
                    # Check if we can place num at pos and pos + num
                    if j < length and seq[j] == 0:
                        seq[pos] = num
                        seq[j] = num
                        used[num] = True
                        if backtrack(pos + 1):
                            return True
                        # backtrack
                        seq[pos] = seq[j] = 0
                        used[num] = False

            # Finally, try placing 1 (only one occurence, distance 0)
            if not used[1]:
                seq[pos] = 1
                used[1] = True
                if backtrack(pos + 1):
                    return True
                seq[pos] = 0
                used[1] = False

            return False

        backtrack(0)
        return seq