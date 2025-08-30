# Leetcode 3302: Find the Lexicographically Smallest Valid Sequence
# https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/
# Solved on 30th of August, 2025
class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        """
        Finds the lexicographically smallest valid sequence of indices from word1 that forms word2.
        :param word1: The source string.
        :param word2: The target string to form.
        :return: A list of integers representing the indices from word1, or an empty list if no valid sequence exists.
        """
        n1 = len(word1)
        n2 = len(word2)

        # Precompute next occurrence of each character
        nextOccurrence = [[-1] * 26 for _ in range(n1 + 1)]
        for i in range(n1 - 1, -1, -1):
            for charCode in range(26):
                nextOccurrence[i][charCode] = nextOccurrence[i + 1][charCode]
            nextOccurrence[i][ord(word1[i]) - ord('a')] = i

        # Compute the baseline greedy sequence with zero mismatches
        lArray = [-1] * n2
        currentIndex = -1
        lIsValid = True
        for i in range(n2):
            charNeeded = ord(word2[i]) - ord('a')
            nextIndex = nextOccurrence[currentIndex + 1][charNeeded]
            if nextIndex == -1:
                lIsValid = False
                # Use a sentinel value for invalid parts of the L-array
                for k in range(i, n2):
                    lArray[k] = n1
                break
            lArray[i] = nextIndex
            currentIndex = nextIndex

        # Precompute the possibility of matching suffixes exactly.
        minSuffixStart = [n2] * (n1 + 1)
        for i in range(n1 - 1, -1, -1):
            minSuffixStart[i] = minSuffixStart[i + 1]
            j = minSuffixStart[i]
            if j > 0 and word1[i] == word2[j - 1]:
                minSuffixStart[i] = j - 1

        # Precompute the next index with a different character
        nextNeq = [-1] * n1
        if n1 > 0:
            nextNeq[n1 - 1] = -1
        for i in range(n1 - 2, -1, -1):
            if word1[i] != word1[i + 1]:
                nextNeq[i] = i + 1
            else:
                nextNeq[i] = nextNeq[i + 1]

        # Find the first position 'k' where a mismatch yields a better sequence.
        pivotK = -1
        bestMismatchIndex = -1
        currentIndex = -1
        for k in range(n2):
            lastIndex = currentIndex

            # Find the smallest possible index for a mismatch at position k
            mismatchCandidateIndex = lastIndex + 1
            if mismatchCandidateIndex >= n1:
                break

            if word1[mismatchCandidateIndex] == word2[k]:
                # If the immediate next char matches, find the next non-matching one.
                if word1[mismatchCandidateIndex] != word1[lastIndex + 2] if lastIndex + 2 < n1 else False:
                    nextDiffCharIndex = lastIndex + 2
                else:
                    nextDiffCharIndex = nextNeq[lastIndex + 1] if lastIndex + 1 < n1 else -1

                if nextDiffCharIndex != -1 and word1[nextDiffCharIndex] != word2[k]:
                    mismatchCandidateIndex = nextDiffCharIndex
                else:
                    found = False
                    for charCode in range(26):
                        if chr(ord('a') + charCode) != word2[k]:
                            nextIdx = nextOccurrence[lastIndex + 1][charCode]
                            if nextIdx != -1:
                                if not found or nextIdx < mismatchCandidateIndex:
                                    mismatchCandidateIndex = nextIdx
                                    found = True

                    if not found:
                        mismatchCandidateIndex = -1

            if mismatchCandidateIndex != -1 and mismatchCandidateIndex < lArray[k]:
                # If a smaller index is found, check if the sequence can be completed.
                if minSuffixStart[mismatchCandidateIndex + 1] <= k + 1:
                    pivotK = k
                    bestMismatchIndex = mismatchCandidateIndex
                    break

            currentIndex = lArray[k]
            # Break if the L-array path becomes invalid.
            if currentIndex == n1:
                break

        # Construct and return the final sequence.
        if pivotK == -1:
            return lArray if lIsValid else []
        else:
            ans = lArray[:pivotK]

            ans.append(bestMismatchIndex)
            currentIndex = bestMismatchIndex

            for i in range(pivotK + 1, n2):
                charNeeded = ord(word2[i]) - ord('a')
                nextIndex = nextOccurrence[currentIndex + 1][charNeeded]
                ans.append(nextIndex)
                currentIndex = nextIndex

            return ans