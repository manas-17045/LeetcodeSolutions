# Leetcode 3357: Minimize the Maximum Adjacent Element Difference
# https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/
# Solved on 26th of November, 2025
class Solution:
    def minDifference(self, nums: list[int]) -> int:
        """
        Minimizes the maximum adjacent element difference in an array by replacing -1s.

        The function aims to replace all occurrences of -1 in the input array `nums`
        with integers such that the maximum absolute difference between any two
        adjacent elements in the modified array is minimized.

        Args:
            nums: A list of integers where some elements might be -1.
        Returns:
            The minimum possible value for the maximum adjacent element difference.
        """
        n = len(nums)
        fixed_diff = 0

        # Determine the minimum bounds for binary search based on fixed adjacencies
        for i in range(n - 1):
            if nums[i] != -1 and nums[i + 1] != -1:
                fixed_diff = max(fixed_diff, abs(nums[i] - nums[i + 1]))

        # Precompute gap constraints and boundary values
        gaps = []  # Stores (min_val, max_val, is_single_length_gap)
        v_min = float('inf')
        v_max = float('-inf')

        i = 0
        while i < n:
            if nums[i] == -1:
                start = i
                while i < n and nums[i] == -1:
                    i += 1
                end = i - 1

                # Identify neighbors of the -1 sequence
                left_val = nums[start - 1] if start > 0 else -1
                right_val = nums[end + 1] if end < n - 1 else -1

                # Update global min/max of boundary values
                if left_val != -1:
                    v_min = min(v_min, left_val)
                    v_max = max(v_max, left_val)
                if right_val != -1:
                    v_min = min(v_min, right_val)
                    v_max = max(v_max, right_val)

                is_single = (start == end)

                # Define constraints based on neighbors
                if left_val != -1 and right_val != -1:
                    # Internal gap: constrained by both sides
                    gaps.append((min(left_val, right_val), max(left_val, right_val), is_single))
                elif left_val != -1:
                    # Boundary gap: constrained only by left
                    gaps.append((left_val, left_val, False))
                elif right_val != -1:
                    # Boundary gap: constrained only by right
                    gaps.append((right_val, right_val, False))
            else:
                i += 1

        # If there are no -1s or no fixed numbers adjacent to -1s
        if v_min == float('inf'):
            return fixed_diff

        def check(d):
            if d < fixed_diff:
                return False

            # --- Strategy 1: Decoupled ---
            # Attempt to cover all gaps with 2 independent numbers x and y.
            # Each gap implies an interval constraint: [max(L,R)-d, min(L,R)+d]
            intervals = []
            possible_decoupled = True

            for l, r, _ in gaps:
                # Interval logic:
                # We need z such that |z-l|<=d and |z-r|<=d
                # z <= l+d, z >= l-d, z <= r+d, z >= r-d
                # Intersection is [max(l,r)-d, min(l,r)+d]
                # Here l is min_val, r is max_val, so interval is [r-d, l+d]
                start_interval = r - d
                end_interval = l + d

                if start_interval > end_interval:
                    possible_decoupled = False
                    break
                intervals.append((start_interval, end_interval))

            if possible_decoupled:
                # Check if 2 points can hit all intervals (Greedy approach)
                intervals.sort(key=lambda x: x[1])
                points_needed = 0
                last_hit = float('-inf')

                for s, e in intervals:
                    if s > last_hit:
                        points_needed += 1
                        last_hit = e

                if points_needed <= 2:
                    return True

            # --- Strategy 2: Coupled ---
            # Attempt to use x and y such that |x - y| <= d.
            # This allows bridging gaps of length >= 2.
            # Combined range of x and y covers ~3d.

            # 1. Global range check
            if v_max - v_min > 3 * d:
                return False

            # 2. Canonical choice for x and y to maximize coverage
            x = v_min + d
            y = v_max - d

            # 3. Check specific constraints for length-1 gaps
            # Length-1 gaps MUST be covered by a single value (x or y), cannot bridge.
            for l, r, is_single in gaps:
                if is_single:
                    # Check if x covers both L and R
                    covered_by_x = (abs(x - l) <= d and abs(x - r) <= d)
                    # Check if y covers both L and R
                    covered_by_y = (abs(y - l) <= d and abs(y - r) <= d)

                    if not covered_by_x and not covered_by_y:
                        return False

            return True

        # Binary Search for the minimum difference
        low, high = 0, 10 ** 9
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans