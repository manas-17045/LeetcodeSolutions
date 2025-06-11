# Leetcode 3445: Maximum Difference Between Even and Odd Frequency II
# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/
# Solved on 11th of June, 2025
import math


class FenwickTreeMin:
    def __init__(self, size):
        self.size = size
        self.tree = [math.inf] * size

    def update(self, idx, val):
        while idx < self.size:
            self.tree[idx] = min(self.tree[idx], val)
            idx |= idx + 1

    def query(self, idx):
        min_val = math.inf
        while idx >= 0:
            min_val = min(min_val, self.tree[idx])
            idx = (idx & (idx + 1)) - 1
        return min_val

    def reset(self):
        self.tree = [math.inf] * self.size

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        """
        Calculates the maximum difference between the counts of two distinct characters 'a' and 'b'
        within a substring of length k, such that the parity of the count of 'a' in the substring
        is odd and the parity of the count of 'b' in the substring is even.

        The characters 'a' and 'b' are chosen from the set {'0', '1', '2', '3', '4'}.

        Args:
            s: The input string consisting of characters '0' through '4'.
            k: The required length of the substring.

        Returns:
            The maximum difference found, or -1 if no such substring exists.
        """
        ans = -math.inf
        chars = "01234"
        n = len(s)

        all_prefix_counts = [[0] * (n + 1) for _ in range(5)]
        for char_code in range(5):
            char_val = chars[char_code]
            for i in range(n):
                all_prefix_counts[char_code][i + 1] = all_prefix_counts[char_code][i] + (1 if s[i] == char_val else 0)

        trees = [[FenwickTreeMin(n + 1) for _ in range(2)] for _ in range(2)]

        for a_code in range(5):
            for b_code in range(5):
                if a_code == b_code:
                    continue

                for r in range(2):
                    for c in range(2):
                        trees[r][c].reset()

                prefixA = all_prefix_counts[a_code]
                prefixB = all_prefix_counts[b_code]

                trees[0][0].update(0, 0)

                for j in range((k - 1), n):
                    start_prefix_idx = j - k + 1

                    pa_start = prefixA[start_prefix_idx] % 2
                    pb_start = prefixB[start_prefix_idx] % 2
                    val_start = prefixA[start_prefix_idx] - prefixB[start_prefix_idx]
                    pcb_start = prefixB[start_prefix_idx]

                    trees[pa_start][pb_start].update(pcb_start, val_start)

                    pa_end = prefixA[j + 1] % 2
                    pb_end = prefixB[j + 1] % 2
                    val_end = prefixA[j + 1] - prefixB[j + 1]
                    pcb_end = prefixB[j + 1]

                    required_pa_start = 1 - pa_end
                    required_pb_start = pb_end

                    tree_to_query = trees[required_pa_start][required_pb_start]

                    best_start_val = tree_to_query.query(pcb_end - 1)

                    if best_start_val != math.inf:
                        current_diff = val_end - best_start_val
                        ans = max(ans, current_diff)

        return ans if ans > -math.inf else -1