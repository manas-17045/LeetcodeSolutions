# Leetcode 3117: Minimum Sum of Values by Dividing Array
# https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/
# Solved on 31st of May, 2025

class Solution:
    def minimumValueSum(self, nums: list[int], andValues: list[int]) -> int:
        """
        Calculates the minimum sum of values of segments such that the bitwise AND of each segment
        equals the corresponding value in `andValues`.

        Args:
            nums: A list of integers.
            andValues: A list of integers representing the required bitwise AND value for each segment.

        Returns:
            The minimum possible sum of segment values, or -1 if it's not possible to partition
            `nums` according to the `andValues` constraints.

        This solution uses dynamic programming with segment trees for efficient range minimum queries.
        """
        n = len(nums)
        m = len(andValues)
        INF = 10**30

        # dp_prev[j] = minimum sum for dividing the first j elements into (i-1) segments
        dp_prev = [INF] * (n + 1)
        dp_prev[0] = 0  # zero elements, zero segments has cost 0

        # Build a segment‐tree over a length‐(n+1) array for range‐minimum queries
        def buildSegtree(arr: list[int]):
            size = 1
            while size < len(arr):
                size <<= 1
            seg = [INF] * (2 * size)
            # copy leaves
            for i in range(len(arr)):
                seg[size + i] = arr[i]
            # build internal nodes
            for i in range(size - 1, 0, -1):
                a = seg[2 * i]
                b = seg[2 * i + 1]
                seg[i] = a if a < b else b
            return seg, size

        # Query the segment‐tree 'seg' of leaf‐size 'segsize' for the minimum over [l..r] (inclusive)
        def query_min(seg: list[int], segsize: int, l: int, r: int) -> int:
            res = INF
            l += segsize
            r += segsize
            while l <= r:
                if (l & 1) == 1:
                    if seg[l] < res:
                        res = seg[l]
                    l += 1
                if (r & 1) == 0:
                    if seg[r] < res:
                        res = seg[r]
                    r -= 1
                l >>= 1
                r >>= 1
            return res

        # We will iterate segment‐count i from 1..m, building dp_curr from dp_prev each time.
        for i in range(1, m + 1):
            target = andValues[i - 1]

            # Build a segment tree over dp_prev so we can do O(log n) range‐min queries
            segTree, segSize = buildSegtree(dp_prev)

            dp_curr = [INF] * (n + 1)
            # We'll maintain a list "prevs" of tuples (val, s_left, s_right), meaning:
            #   For each distinct AND‐value val among subarrays ending at index (j-1),
            #   all starting positions s in [s_left..s_right] (1‐based) satisfy:
            #       AND(nums[s-1..(j-1)]) == val.
            prevs = []

            # Process j = 1..n as the right endpoint of the i‐th segment
            for j in range(1, n + 1):
                x = nums[j - 1]
                curr_map = {}

                # 1) Propagate all previous AND‐intervals up to index (j-1) ⇒ now extended to j
                for (val_prev, l_prev, r_prev) in prevs:
                    new_val = val_prev & x
                    if new_val in curr_map:
                        ll, rr = curr_map[new_val]
                        if l_prev < ll:
                            ll = l_prev
                        if r_prev > rr:
                            rr = r_prev
                        curr_map[new_val] = (ll, rr)
                    else:
                        curr_map[new_val] = (l_prev, r_prev)

                # 2) Add the single‐element subarray [j..j], whose AND is x and start = end = j
                if x in curr_map:
                    ll, rr = curr_map[x]
                    if j < ll:
                        ll = j
                    if j > rr:
                        rr = j
                    curr_map[x] = (ll, rr)
                else:
                    curr_map[x] = (j, j)

                # 3) Convert curr_map into "prevs" (a small list of (val, s_left, s_right))
                prevs = [(val, interval[0], interval[1]) for val, interval in curr_map.items()]

                # 4) If the desired AND = target is present among these intervals,
                #    we can form the i‐th segment from some start s in [l..r] ending at j.
                if target in curr_map:
                    l, r = curr_map[target]  # 1‐based range of valid starts
                    left = l - 1  # convert to dp_prev index (0‐based)
                    right = r - 1
                    if left <= right:
                        best_prev = query_min(segTree, segSize, left, right)
                        if best_prev < INF:
                            dp_curr[j] = best_prev + x

            # Move to the next layer: dp_prev ← dp_curr
            dp_prev = dp_curr

        ans = dp_prev[n]
        return ans if ans < INF else -1