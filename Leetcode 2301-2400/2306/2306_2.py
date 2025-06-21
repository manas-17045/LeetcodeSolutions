# Leetcode 2306: Naming a Company
# https://leetcode.com/problems/naming-a-company/
# Solved on 21st of June, 2025

class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        """
        Calculates the number of distinct names that can be formed by swapping the first letters
        of two existing ideas.

        Args:
            ideas: A list of strings representing existing ideas.

        Returns:
            An integer representing the total number of distinct names that can be formed.

        The solution uses a bucket-based approach to group suffixes by their starting letter.
        """
        # Build 26 sets of suffixes, one per starting letter
        buckets = [set() for _ in range(26)]
        for word in ideas:
            idx = ord(word[0]) - ord('a')
            buckets[idx].add(word[1:])

        ans = 0
        # For each unordered pair of buckets (i, j), i < j
        for i in range(26):
            si= buckets[i]
            if not si:
                continue
            for j in range((i + 1), 26):
                sj = buckets[j]
                if not sj:
                    continue
                # Iterate over the smaller set for a tiny speedup
                if len(si) < len(sj):
                    common = sum(1 for suf in si if suf in sj)
                else:
                    common = sum(1 for suf in sj if suf in si)

                ans += 2 * (len(si) - common) * (len(sj) - common)

        return ans