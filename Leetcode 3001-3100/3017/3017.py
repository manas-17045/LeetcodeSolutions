# Leetcode 3017: Count the Number of Houses at a Certain Distance II
# https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/
# Solved on 12th of December, 2025
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        """
        Calculates the number of pairs of houses at a certain distance for all possible distances.

        Args:
            n: The total number of houses.
            x: One of the special houses.
            y: The other special house.
        Returns:
            A list where the i-th element is the number of pairs of houses with distance i+1.
        """
        if x > y:
            x, y = y, x

        if y - x <= 1:
            return [2 * (n - i) for i in range(1, n + 1)]

        diff = [0] * (n + 2)

        def add(l, r):
            if l > r:
                return
            diff[l] += 1
            diff[r + 1] -= 1

        for i in range(1, n + 1):
            if i >= y:
                add(1, n - i)
            elif i < x:
                m = (x + y + 1) // 2
                add(1, m - i)
                add(x - i + 2, x + y - i - m)
                add(x - i + 1, x - i + 1 + n - y)
            else:
                limit = i + (y - x + 1) // 2
                upper_linear = min(y, limit)
                add(1, upper_linear - i)
                add(i - x + 1, i + y - x - upper_linear)

                dist_to_y = min(y - i, i - x + 1)
                add(dist_to_y + 1, dist_to_y + n - y)

        res = []
        curr = 0
        for k in range(1, n + 1):
            curr += diff[k]
            res.append(curr * 2)

        return res