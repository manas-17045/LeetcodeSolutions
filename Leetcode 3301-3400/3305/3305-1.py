# Leetcode 3305: Count of Substrings Containing Every Vowel and K Consonants I
# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/
# Solved on 17th of October, 2025
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        """
        Counts the number of substrings in 'word' that contain every vowel ('a', 'e', 'i', 'o', 'u')
        and exactly 'k' consonants.
        :param word: The input string.
        :param k: The exact number of consonants required.
        :return: The total count of such substrings.
        """
        def countWithAtLeast(consonantTarget: int) -> int:
            result = 0
            vowels = "aeiou"

            lastVowelPos = {v: -1 for v in vowels}
            consonantIndices = []

            for right, char in enumerate(word):
                if char in vowels:
                    lastVowelPos[char] = right
                else:
                    consonantIndices.append(right)

                vowelWindowStart = min(lastVowelPos.values())
                if vowelWindowStart == -1:
                    continue

                if len(consonantIndices) < consonantTarget:
                    continue

                consonantWindowStart = -1
                if consonantTarget == 0:
                    consonantWindowStart = right
                else:
                    consonantWindowStart = consonantIndices[len(consonantIndices) - consonantTarget]

                validStartUpto = min(vowelWindowStart, consonantWindowStart)
                result += validStartUpto + 1

            return result

        countForK = countWithAtLeast(k)
        countForKPlus1 = countWithAtLeast(k + 1)

        return countForK - countForKPlus1