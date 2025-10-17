# Leetcode 3305: Count of Substrings Containing Every Vowel and K Consonants I
# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/
# Solved on 17th of October, 2025
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        """
        Counts the number of substrings in 'word' that contain all five vowels ('a', 'e', 'i', 'o', 'u')
        and have at least 'k' consonants.
        :param word: The input string.
        :param k: The minimum number of consonants required.
        :return: The total count of such substrings.
        """
        n = len(word)
        if n < 5:
            return 0

        # Map vowels to indices for quick counting
        vow_idx = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

        def at_least(t: int) -> int:
            counts = [0] * 5
            cons = 0
            left = 0
            res = 0

            for right, ch in enumerate(word):
                if ch in vow_idx:
                    counts[vow_idx[ch]] += 1
                else:
                    cons += 1

                while all(c > 0 for c in counts) and cons >= t:
                    chL = word[left]
                    if chL in vow_idx:
                        counts[vow_idx[chL]] -= 1
                    else:
                        cons -= 1
                    left += 1

                res += left
            return res

        return at_least(k) - at_least(k + 1)