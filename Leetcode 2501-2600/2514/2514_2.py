# Leetcode 2514: Count Anagrams
# https://leetcode.com/problems/count-anagrams/
# Solved on 15th of June, 2025

class Solution:
    def countAnagrams(self, s: str) -> int:
        """
        Counts the total number of distinct anagrams of a string `s`, where each word in `s` is treated independently.

        The problem asks for the number of ways to rearrange the letters within each word of the input string `s`
        such that the resulting string is different from other possible rearrangements. The words themselves maintain
        their relative order.

        For each word, the number of distinct anagrams is given by the multinomial coefficient:
        (length of word)! / (count of char1)! * (count of char2)! * ...

        The total number of distinct anagrams for the entire string `s` is the product of the number of distinct
        anagrams for each word.

        We use modular arithmetic to handle potentially large results.
        """
        mod = 10**9 + 7

        # Split into words and compute the maximum word length
        words = s.split(' ')
        max_len = max(len(w) for w in words)

        # Precompute factorials and inverse-factorials up to max_len
        fact = [1] * (max_len + 1)
        for i in range(1, (max_len + 1)):
            fact[i] = (fact[i - 1] * i) % mod

        inv_fact = [1] * (max_len + 1)
        inv_fact[max_len] = pow(fact[max_len], (mod - 2), mod)
        for i in range(max_len, 0, -1):
            inv_fact[i - 1] = (inv_fact[i] * i) % mod

        # Helper function to compute number of distinct permutations of a single word
        def countPermutations(word: str) -> int:
            cnt = {}
            for ch in word:
                cnt[ch] = cnt.get(ch, 0) + 1

            res = fact[len(word)]
            for c in cnt.values():
                res = (res * inv_fact[c]) % mod

            return res

        # Multiply the counts for each word
        ans = 1
        for w in words:
            ans = ans * countPermutations(w) % mod

        return ans