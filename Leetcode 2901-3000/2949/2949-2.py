# Leetcode 2949: Count Beautiful Substrings II
# https://leetcode.com/problems/count-beautiful-substrings-ii/
# Solved on 14th of October, 2025
from collections import defaultdict


class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        """
        Calculates the number of "beautiful" substrings in a given string s.
        A substring is beautiful if the number of vowels and consonants are equal,
        and the product of the number of vowels and consonants is divisible by k.
        :param s: The input string.
        :param k: The divisor for the product of vowels and consonants.
        :return: The total count of beautiful substrings.
        """
        if k == 1:
            m = 1
        else:
            temp = k
            m = 1
            p = 2
            while p * p <= temp:
                if temp % p == 0:
                    e = 0
                    while temp % p == 0:
                        temp //= p
                        e += 1
                    m *= p ** ((e + 1) // 2)
                p += 1 if p == 2 else 2

            if temp > 1:
                # Remaining prime
                e = 1
                m *= temp **((e + 1) // 2)

        # Count prefixes
        vowels = set('aeiou')
        counts = defaultdict(int)

        counts[(0, 0)] = 1
        pv = 0
        ans = 0

        for i, ch in enumerate(s):
            if ch in vowels:
                pv += 1
            pos = i + 1
            diff = pv - (pos - pv)
            a = pv % m if m != 0 else 0
            ans += counts.get((diff, a), 0)
            counts[(diff, a)] += 1

        return ans