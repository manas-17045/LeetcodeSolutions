# Leetcode 2785: Sort Vowels in a String
# https://leetcode.com/problems/sort-vowels-in-a-string/
# Solved on 11th of September, 2025
class Solution:
    def sortVowels(self, s: str) -> str:
        """
        Sorts the vowels within a given string `s` in ascending ASCII order,
        while keeping the consonants in their original positions.
        :param s: The input string.
        :return: The string with vowels sorted and consonants in place.
        """
        vowels_set = set('aeiouAEIOU')
        # Collect vowels in original order
        vowels = [ch for ch in s if ch in vowels_set]
        # Sort vowels by ASCII
        vowels.sort()
        # Place sorted vowels back into vowel positions
        res = []
        vi = 0
        for ch in s:
            if ch in vowels_set:
                res.append(vowels[vi])
                vi += 1
            else:
                res.append(ch)

        return ''.join(res)