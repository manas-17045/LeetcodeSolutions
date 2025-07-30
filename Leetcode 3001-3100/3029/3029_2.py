# Leetcode 3029: Minimum Time to Revert Word to Initial State I
# https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i/
# Solved on 30th of July, 2025
class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        """
        Calculates the minimum time to return a word to its initial state by repeatedly
        removing the first 'k' characters and appending them to the end.
        :param word: The input string.
        :param k: The number of characters to remove and append in each operation.
        :return: The minimum number of operations (time) to reach the initial state.
        """
        n = len(word)
        Z = [0] * n
        Z[0] = n
        l = r = 0
        for i in range(1, n):
            if i <= r:
                Z[i] = min(r - i + 1, Z[i - l])

            while i + Z[i] < n and word[Z[i]] == word[i + Z[i]]:
                Z[i] += 1

            if i + Z[i] - 1 > r:
                l = i
                r = i + Z[i] - 1

        max_t = (n + k - 1) // k
        for t in range(1, max_t + 1):
            offset = t * k
            if offset >= n:
                return t

            if Z[offset] >= n - offset:
                return t

        return max_t