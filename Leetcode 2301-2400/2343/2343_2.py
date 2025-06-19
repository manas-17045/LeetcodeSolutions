# Leetcode 2343: Query Kth Smallest Trimmed Number
# https://leetcode.com/problems/query-kth-smallest-trimmed-number/
# Solved on 18th of June, 2025

class Solution:
    def smallestTrimmedNumbers(self, nums: list[str], queries: list[list[str]]) -> list[int]:
        """
        For each query [k, trim], we need to find the index of the k-th smallest number
        after trimming each number to its rightmost 'trim' digits.

        The approach is to pre-process the numbers for each unique trim length
        specified in the queries. For each trim length 't', we create a list of
        pairs (trimmed_string, original_index) and sort this list lexicographically
        based on the trimmed string, using the original index as a tie-breaker.
        We then store the sorted list of original indices.

        Finally, for each query [k, t], we simply look up the (k-1)-th index
        in the pre-computed sorted list for trim length 't'.

        Args:
            nums: A list of strings representing the numbers.
            queries: A list of queries, where each query is [k, trim].
        Returns: A list of integers, where each integer is the answer to the corresponding query.
        """
        n = len(nums)
        # Gather all trim lengths we'll need
        needed_trims = {trim for _, trim in queries}

        # For each trim length t, compute a list of indices
        # sorted by (trimmed_string, original_index)
        trim_to_sorted_indices = {}
        for t in needed_trims:
            trimmed_pairs = []
            # Build (trimmed_suffix, idx) for each number
            for idx, num in enumerate(nums):
                trimmed_pairs.append((num[-t:], idx))
            # Sort lex on the suffix, tie-breaking by idx
            trimmed_pairs.sort()
            # Store just the indices in sorted order
            trim_to_sorted_indices[t] = [idx for _, idx in trimmed_pairs]

        # Now, answer each query
        answer = []
        for k, t in queries:
            # k is 1-indexed; we want the (k - 1)-th in the sorted list for trim t
            answer.append(trim_to_sorted_indices[t][k - 1])
        return answer