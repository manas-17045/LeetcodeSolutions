# Leetcode 3430: Maximum and Minimum Sums of at Most Size K Subarrays
# https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/
# Solved on 9th of June, 2025

class Solution:
    def minMaxSubarraySum(self, nums: list[int], k: int) -> int:
        """
        Calculates the sum of minimums and maximums of all subarrays of length at least k.

        This solution uses a monotonic stack approach to efficiently find the previous and next
        smaller/larger elements for each element in the array. This information is then used
        to determine the number of subarrays of length at least k where the current element
        is the minimum or maximum. The contribution of each element to the total sum is
        calculated and accumulated.

        Args:
            nums: A list of integers.
            k: The minimum length of the subarrays to consider.

        Returns:
            The sum of the minimums and maximums of all subarrays of length at least k.
        """
        n = len(nums)

        # Build Pmax, Nmax for "max" monotonicity
        Pmax = [-1] * n
        Nmax = [n] * n
        st = []
        for i in range(n):
            while st and nums[st[-1]] <= nums[i]:
                st.pop()
            Pmax[i] = st[-1] if st else -1
            st.append(i)
        st.clear()
        for i in range((n - 1), -1, -1):
            while st and nums[st[-1]] < nums[i]:
                st.pop()
            Nmax[i] = st[-1] if st else n
            st.append(i)

        # Build Pmin, Nmin for "min" monotonicity
        Pmin = [-1] * n
        Nmin = [n] * n
        st.clear()
        for i in range(n):
            while st and nums[st[-1]] >= nums[i]:
                st.pop()
            Pmin[i] = st[-1] if st else -1
            st.append(i)
        st.clear()
        for i in range((n - 1), -1, - 1):
            while st and nums[st[-1]] > nums[i]:
                st.pop()
            Nmin[i] = st[-1] if st else n
            st.append(i)

        # Helper function
        def count_lr(L: int, R: int) -> int:
            x = min(L, R)
            if x <= 0:
                return 0
            # Split point t0 so that for l <= t0, k- l + 1 >= R
            t0 = max(0, k - R + 1)
            u = min(x, t0)
            cnt = R * u

            if x > t0:
                n2 = x - t0
                a = t0 + 1
                b = x
                cnt = n2 * (k + 1) - ((a + b) * n2) // 2

            return cnt

        ans = 0
        # Accumulate contributions
        for i, v in enumerate(nums):
            L = i - Pmax[i]
            R = Nmax[i] - i
            ans += v * count_lr(L, R)
            L = i - Pmin[i]
            R = Nmin[i] - i
            ans += v * count_lr(L, R)

        return ans