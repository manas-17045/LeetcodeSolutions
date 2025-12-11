# Leetcode 2953: Count Complete Substrings
# https://leetcode.com/problems/count-complete-substrings/
# Solved on 11th of December, 2025
class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        """
        Counts the number of "complete" substrings in a given word.
        A substring is considered complete if all its characters appear exactly k times,
        and the absolute difference between the ASCII values of any two adjacent characters
        in the original word is at most 2.

        Args:
            word (str): The input string.
            k (int): The required frequency for each character in a complete substring.
        Returns:
            int: The total count of complete substrings.
        """
        n = len(word)
        result = 0
        start = 0

        for i in range(1, n + 1):
            if i == n or abs(ord(word[i]) - ord(word[i - 1])) > 2:
                length = i - start
                for m in range(1, 27):
                    windowSize = m * k
                    if windowSize > length:
                        break

                    counts = [0] * 26
                    charsWithK = 0

                    for j in range(start, start + windowSize):
                        idx = ord(word[j]) - 97
                        counts[idx] += 1
                        if counts[idx] == k:
                            charsWithK += 1
                        elif counts[idx] == k + 1:
                            charsWithK -= 1

                    if charsWithK == m:
                        result += 1

                    for j in range(start + windowSize, i):
                        inIdx = ord(word[j]) - 97
                        outIdx = ord(word[j - windowSize]) - 97

                        counts[inIdx] += 1
                        if counts[inIdx] == k:
                            charsWithK += 1
                        elif counts[inIdx] == k + 1:
                            charsWithK -= 1

                        counts[outIdx] -= 1
                        if counts[outIdx] == k:
                            charsWithK += 1
                        elif counts[outIdx] == k - 1:
                            charsWithK -= 1

                        if charsWithK == m:
                            result += 1

                start = i

        return result