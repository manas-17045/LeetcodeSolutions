# Leetcode 3029: Minimum Time to Revert Word to Initial State I
# https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i/
# Solved on 30th of July, 2025
class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        """
        Calculates the minimum time required to revert a word to its initial state
        by repeatedly removing the first 'k' characters and appending them to the end.

        Args:
            word (str): The input word.
            k (int): The number of characters to remove and append in each step.
        Returns:
            int: The minimum time (number of operations) to reach the initial state.
        """

        wordLength = len(word)
        zArray = [0] * wordLength
        left = 0
        right = 0

        for i in range(1, wordLength):
            if i < right:
                zArray[i] = min(right - i, zArray[i - left])

            while i + zArray[i] < wordLength and word[zArray[i]] == word[i + zArray[i]]:
                zArray[i] += 1

            if i + zArray[i] > right:
                left = i
                right = i + zArray[i]

        currentTime = 1
        while currentTime * k < wordLength:
            checkIndex = currentTime * k
            remainingLength = wordLength - checkIndex
            if zArray[checkIndex] >= remainingLength:
                return currentTime
            currentTime += 1

        return (wordLength + k - 1) // k