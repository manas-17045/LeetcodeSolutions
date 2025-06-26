# Leetcode 2663: Lexicographically Smallest Beautiful String
# https://leetcode.com/problems/lexicographically-smallest-beautiful-string/
# Solved on 26th of June, 2025
class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        """
        Finds the lexicographically smallest "beautiful" string that is strictly greater than `s`.

        A string is "beautiful" if:
        1. It consists only of the first `k` lowercase English letters.
        2. It does not contain any palindrome of length 2 or 3.
           (i.e., no 'aa', 'aba', 'bb', 'bcb', etc.)

        Args:
            s: The input string.
            k: The number of allowed characters (first k lowercase letters).
        Returns:
            The lexicographically smallest beautiful string strictly greater than `s`, or an empty string if no such string exists.
        """
        n = len(s)
        # Convert string to a list of character ordinal values for easier manipulation
        sCharsNum = [ord(char) for char in s]

        firstLetterOrd = ord('a')
        maxCharNum = firstLetterOrd + k - 1

        # Iterate from the rightmost character (n - 1) to the leftmost (index 0)
        i = n - 1
        while i >= 0:
            # Start checking from the character numerically greater than sCharsNum[i]
            startCandidateNum = sCharsNum[i] + i

            # Iterate through possible characters for sCharsNum[i]
            for candidateNum in range(startCandidateNum, maxCharNum + 1):
                canPlaceCandidate = True
                # Check against sCharsNums[i - 1]
                if i > 0 and sCharsNum[i - 1] == candidateNum:
                    canPlaceCandidate = False

                # Check against sCharsNums[i - 2] (only if not already invalid and index (i - 2) exists)
                if canPlaceCandidate and i > 1 and sCharsNum[i - 2] == candidateNum:
                    canPlaceCandidate = False

                if canPlaceCandidate:
                    sCharsNum[i] = candidateNum

                    for j in range((i + 1), n):
                        for fillNum in range(firstLetterOrd, (maxCharNum + 1)):
                            canPlaceFillNum = True

                            if sCharsNum[j - 1] == fillNum:
                                canPlaceFillNum = False

                            if canPlaceFillNum and j > 1 and sCharsNum[j - 2] == fillNum:
                                canPlaceFillNum = False

                            if canPlaceFillNum:
                                sCharsNum[j] = fillNum
                                break

                    # Successfully constructed the lexicographically smallest beautiful string larger than s
                    return "".join([chr(num) for num in sCharsNum])

            i -= 1

        return ""