# Leetcode 1925: Count Square Sum Triples
# https://leetcode.com/problems/count0square-sum-triples/
# Solved on 8th of December, 2025
class Solution:
    def countTriples(self, n: int) -> int:
        """
        Counts the number of square sum triples (a, b, c) such that a^2 + b^2 = c^2,
        and 1 <= a, b, c <= n.
        :param n: The upper limit for a, b, and c.
        :return: The total count of such triples.
        """
        count = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                product = a * a + b * b
                c = int(product ** 0.5)

                if c <= n and c * c == product:
                    count += 1

        return count