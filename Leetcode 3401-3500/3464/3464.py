# Leetcode 3464: Maximize the Distance Between Points on a Square
# https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/
# Solved on 15th of December, 2025
class Solution:
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        """
        Maximizes the minimum distance between k points chosen from the given points on the perimeter of a square.

        Args:
            side (int): The side length of the square.
            points (list[list[int]]): A list of [x, y] coordinates of points on the perimeter of the square.
            k (int): The number of points to choose.
        Returns:
            int: The maximum possible minimum distance between any two chosen points.
        """
        p = []
        # Map 2D boundary points to 1D perimeter coordinates
        for x, y in points:
            if y == 0:
                p.append(x)
            elif x == side:
                p.append(side + y)
            elif y == side:
                p.append(2 * side + (side - x))
            else:
                p.append(3 * side + (side - y))

        p.sort()
        n = len(p)
        perimeter = 4 * side
        # Create extended array for circular processing
        extended = p + [val + perimeter for val in p]
        limit = len(extended)

        # Binary Search for the maximum minimum distance
        low = 1
        high = side
        ans = 1

        # Determine height of the lifting table
        jumps_needed = k - 1
        log_k = jumps_needed.bit_length()

        while low <= high:
            mid = (low + high) // 2

            # Sliding window to find nearest valid next point for each point
            next_idx = [0] * limit
            r = 0
            for i in range(limit):
                target = extended[i] + mid
                while r < limit and extended[r] < target:
                    r += 1
                next_idx[i] = r

            # Build Binary Lifting Table
            lift = [[next_idx[i]] for i in range(limit)]

            for j in range(1, log_k):
                for i in range(limit):
                    mid_jump = lift[i][-1]
                    if mid_jump >= limit:
                        lift[i].append(limit)
                    else:
                        lift[i].append(lift[mid_jump][j - 1])

            possible = False
            for i in range(n):
                curr = i
                # Jump k-1 times using binary lifting
                for bit in range(log_k):
                    if (jumps_needed >> bit) & 1:
                        curr = lift[curr][bit]
                        if curr >= limit:
                            break

                # Check if the chain fits within the perimeter (circular constraint)
                if curr < limit:
                    if extended[i + n] - extended[curr] >= mid:
                        possible = True
                        break

            if possible:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans