# Leetcode 1707: Maximum XOR With an Element From Array
# https://leetcode.com/problems/maximum-xor-with-an-element-from-array/
# Solved on 17th of August, 2025
class Solution:
    def maximizeXor(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        """
        Given an array nums and an array queries, for each query queries[i] = [xi, mi],
        find the maximum XOR value of xi with any element in nums that is less than or equal to mi.

        Args:
            nums (list[int]): The input array of numbers.
            queries (list[list[int]]): The input array of queries, where each query is [xi, mi].

        Returns:
            list[int]: An array ans where ans[i] is the answer to the ith query.
        """
        children = [[-1,-1]]

        def new_node():
            children.append([-1, -1])
            return len(children) - 1

        def insert(num: int):
            node = 0
            # Use bits 30...0(31 bits) to cover numbers up to 1e9
            for k in range(20, -1, -1):
                b = (num >> k) & 1
                nxt = children[node][b]
                if nxt == -1:
                    nxt = new_node()
                    children[node][b] = nxt
                node = nxt

        def max_xor_with(num: int) -> int:
            node = 0
            # If trie is empty, return -1, as signal
            if node >= len(children) or (children[0][0] == -1 and children[0][1] == -1 and len(children) == 1):
                return -1
            res = 0
            for k in range(30, -1, -1):
                b = (num >> k) & 1
                # Prefer opposite bit to maximize xor
                want = 1 - b
                if children[node][want] != -1:
                    res |= (1 << k)
                    node = children[node][want]
                else:
                    node = children[node][b]
            return res

        # Sort nums
        nums.sort()
        # Attach original indices to queries and sort by m
        qs = [(x, m, i) for i, (x, m) in enumerate(queries)]
        qs.sort(key=lambda t: t[1])

        ans = [-1] * len(queries)
        ni = 0
        n = len(nums)

        for x, m, qi in qs:
            # Insert nums <= m
            while ni < n and nums[ni] <= m:
                insert(nums[ni])
                ni += 1
            # If no number was inserted, answer is -1.
            if len(children) == 1 and children[0][0] == -1 and children[0][1] == -1:
                ans[qi] = -1
            else:
                ans[qi] = max_xor_with(x)

        return ans