# Leetcode 3106: Lexicographically Smallest String After Operations With Constraint
# https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/
# Solved on 18th of June, 2025

class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        n = len(s)
        """
        Given a string s and an integer k, return the lexicographically smallest string
        that can be obtained by changing at most k characters in s.

        A change consists of changing a character to any other character.
        The cost of changing a character ch1 to ch2 is the minimum number of operations
        to change ch1 to ch2. An operation consists of changing a character to its
        adjacent character in the alphabet (wrapping around from 'z' to 'a' and 'a' to 'z').

        """
        n = len(s)
        # We'll build the result in a list for efficiency
        t = []

        for i, ch in enumerate(s):
            if k == 0:
                # No operations left, just copy the rest
                t.append(s[i:])
                break

            val = ord(ch) - ord('a')
            # Cost to change ch to 'a' by going backward or wrapping forward
            back_cost = val     # Cost to go backward down to 'a'
            forward_cost = 26 - val     # Cost to wrap forward up to 'a'
            cost_to_a = min(back_cost, forward_cost)

            if cost_to_a <= k:
                # We can turn ch into 'a'
                t.append('a')
                k -= cost_to_a
            else:
                # Can't reach 'a'; use all remaining k to move ch backward
                # (moving forward would only increase ch lexically)
                new_val = val - k
                t.append(chr(new_val + ord('a')))
                k = 0
                # Copy the rest verbatim and break
                t.append(s[(i + 1):])
                break

        # If we never filled in any tail copy, join what we've got
        return "".join(t)