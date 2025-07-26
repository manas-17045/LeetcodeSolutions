# Leetcode 2407: Longest Increasing Subsequence II
# https://leetcode.com/problems/longest-increasing-subsequence-ii/
# Solved on 26th of July, 2025
class SegmentTree:
    def __init__(self, n: int):
        # build on [0..n-1]
        self.n = n
        self.size = 1
        while self.size < n:
            self.size <<= 1
        self.tree = [0] * (2 * self.size)

    def update(self, pos: int, val: int) -> None:
        # point-update: tree[pos] = max(tree[pos], val)
        i = pos + self.size
        if self.tree[i] >= val:
            return
        self.tree[i] = val
        i >>= 1
        while i:
            self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])
            i >>= 1

    def query(self, l: int, r: int) -> int:
        # range-max over [l..r], inclusive
        if l > r:
            return 0
        res = 0
        l += self.size
        r += self.size
        while l <= r:
            if (l & 1):
                res = max(res, self.tree[l])
                l += 1
            if not (r & 1):
                res = max(res, self.tree[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res

class Solution:
    def lengthOfLIS(self, nums: list[int], k: int) -> int:
        """
        Calculates the length of the longest increasing subsequence (LIS) such that the difference
        between adjacent elements in the subsequence is at most k.

        Args:
            nums: A list of integers.
            k: The maximum allowed difference between adjacent elements in the LIS.

        Returns:
            The length of the longest increasing subsequence satisfying the condition.
        """
        if not nums:
            return 0

        max_val = max(nums)
        st = SegmentTree(max_val + 1)
        ans = 0

        for x in nums:
            # We only consider previous endings in [x-k, x-1]
            left = max(1, x - k)
            best_prev = st.query(left, x - 1)
            curr = best_prev + 1
            # Record dp[x] = curr
            st.update(x, curr)
            ans = max(ans, curr)

        return ans