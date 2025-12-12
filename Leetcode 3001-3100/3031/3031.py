# Leetcode 3031: Minimum Time to Revert Word to Initial State II
# https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/
# Solved on 12th of December, 2025
class Solution:
    def minimumTimetoInitialState(self, word: str, k: int) -> int:
        """
        Calculates the minimum time to revert a word to its initial state.

        Args:
            word (str): The input word.
            k (int): The number of characters to remove from the beginning in each operation.

        Returns:
            int: The minimum number of operations required to revert the word to its initial state.
        """
        n = len(word)
        lps = [0] * n
        currentLength = 0
        i = 1

        while i < n:
            if word[i] == word[currentLength]:
                currentLength += 1
                lps[i] = currentLength
                i += 1
            else:
                if currentLength != 0:
                    currentLength = lps[currentLength - 1]
                else:
                    lps[i] = 0
                    i += 1

        maxLength = lps[n - 1]

        while maxLength > 0:
            if (n - maxLength) % k == 0:
                return (n - maxLength) // k
            maxLength = lps[maxLength - 1]

        return (n + k - 1) // k