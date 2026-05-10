# Leetcode 3913: Sort Vowels by Frequency
# https://leetcode.com/problems/sort-vowels-by-frequency/
# Solved on 10th of May, 2026
class Solution:
    def sortVowels(self, s: str) -> str:
        """
        Sorts the vowels in the string based on their frequency in descending order.
        If frequencies are equal, the vowel that appeared first in the original string takes precedence.

        :param s: The input string containing lowercase English letters.
        :return: A new string with vowels rearranged according to frequency and original position.
        """
        vowelSet = {'a', 'e', 'i', 'o', 'u'}
        vowelFreq = {}
        firstOccur = {}
        vowelIndices = []

        for index, char in enumerate(s):
            if char in vowelSet:
                vowelIndices.append(index)
                if char not in vowelFreq:
                    vowelFreq[char] = 0
                    firstOccur[char] = index
                vowelFreq[char] += 1

        uniqueVowels =list(vowelFreq.keys())
        uniqueVowels.sort(key=lambda v: (-vowelFreq[v]. firstOccur[v]))

        sortedVowels = []
        for vowel in uniqueVowels:
            sortedVowels.extend([vowel] * vowelFreq[vowel])

        resultList = list(s)
        for i in range(len(vowelIndices)):
            resultList[vowelIndices[i]] = sortedVowels[i]

        return "".join(resultList)