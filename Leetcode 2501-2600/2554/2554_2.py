# Leetcode 2554: Maximum Number of Integers to Choose From a Range I
# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/
# Solved on 9th of August, 2025
class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        """
        Calculates the maximum count of distinct integers from 1 to n that can be chosen such that their sum does not exceed maxSum,
        excluding any integers present in the banned list.
        :param banned: A list of integers that cannot be chosen.
        :param n: The upper limit for integers that can be chosen (integers are from 1 to n).
        :param maxSum: The maximum allowed sum of the chosen integers.
        :return: The maximum count of distinct integers that can be chosen.
        """
        # Keep only banned numbers inside [1, n], unique and sorted
        banned_sorted = sorted(set(x for x in banned if 1 <= x <= n))

        def max_take_from_segment(L: int, seg_len: int, rem: int) -> (int, int):

            if seg_len <= 0 or rem < L:
                return 0, 0
            lo, hi = 0, seg_len
            while lo < hi:
                mid = (lo + hi + 1) // 2
                s = mid * (2 * L + mid - 1) // 2
                if s <= rem:
                    lo = mid
                else:
                    hi = mid - 1

            if lo == 0:
                return 0, 0
            s_lo = lo * (2 * L + lo - 1) // 2
            return lo, s_lo

        curr = 1
        count = 0
        rem = maxSum

        for b in banned_sorted:
            if curr > n or rem <= 0:
                break
            end = b - 1
            if end >= curr:
                seg_len = end - curr + 1
                taken, used = max_take_from_segment(curr, seg_len, rem)
                count += taken
                rem -= used
                curr += taken
                if rem <= 0:
                    return count
                # If we consumed the whole segment, move curr past it to the banned number
                if taken == seg_len:
                    # Skip the banned number itself
                    curr = end + 1
                else:
                    # Cannot take more from this segment because rem exhausted for next number
                    return count
            else:
                # No available numbers before this banned number
                curr = max(curr, b + 1)

        # Final segment after all banned numbers
        if curr <= n and rem > 0:
            seg_len = n - curr + 1
            taken, used = max_take_from_segment(curr, seg_len, rem)
            count += taken

        return count