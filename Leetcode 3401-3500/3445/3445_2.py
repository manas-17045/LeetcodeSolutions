# Leetcode 3445: Maximum Difference Between Even and Odd Frequency II
# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/
# Solved on 11th of June, 2025

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        """
        Calculates the maximum difference between the count of two distinct digits 'a' and 'b'
        within a substring of length at least k, where the substring is formed by removing
        a prefix from a larger substring.

        Args:
            s: The input string consisting of digits '0' through '4'.
            k: The minimum length of the substring.

        Returns:
            The maximum difference found.
        """
        # Initialize answer to a very small number
        ans = -10**18
        n = len(s)

        # Iterate over all ordered pairs of distinct characters in '0'...'4'
        for a, b in self.getPermutations():
            minDiff = [[10**18, 10**18], [10**18, 10**18]]

            # Prefix counts of a and b
            prefixA = [0]
            prefixB = [0]

            l = 0
            for r in range(n):
                prefixA.append(prefixA[-1] + (1 if s[r] == a else 0))
                prefixB.append(prefixB[-1] + (1 if s[r] == b else 0))

                # Try to shrink the window from the left
                while (r - l + 1) >= k and prefixA[l] < prefixA[-1] and prefixB[l] < prefixB[-l]:
                    pa = prefixA[l] % 2
                    pb = prefixB[l] % 2
                    diff = prefixA[l] - prefixB[l]
                    # Record the minimum diff seen for this parity combination
                    if diff < minDiff[pa][pb]:
                        minDiff[pa][pb] = diff
                    l += 1

                # Compute candidate answer ending at r
                cur_pa = prefixA[-1] % 2
                cur_pb = prefixB[-1] % 2
                # We want a starting prefix with opposite a-parity
                needed_pa = 1 - cur_pa
                cand = (prefixA[-1] - prefixB[-1]) - minDiff[needed_pa][cur_pb]
                if cand > ans:
                    ans = cand

        return ans

    def getPermutations(self) -> list[tuple[str, str]]:
        chars = "01234"
        perms = []
        for i in range(len(chars)):
            for j in range(len(chars)):
                if i != j:
                    perms.append((chars[i], chars[j]))
        return perms