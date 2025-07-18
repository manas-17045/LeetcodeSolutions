# Leetcode 2019: The Score of Students Solving Math Expression
# https://leetcode.com/problems/the-score-of-students-solving-math-expressions/
# Solved on 18th of July, 2025
from functools import lru_cache


class Solution:
    def scoreOfStudents(self, s: str, answers: list[int]) -> int:
        """
        Calculates the score of students based on their answers to an arithmetic expression.

        :param s: The arithmetic expression as a string.
        :param answers: A list of integer answers provided by students.
        :return: The total score of the students.
        """
        toks = []
        for ch in s:
            if ch.isdigit():
                toks.append(int(ch))
            else:
                toks.append(ch)

        # First pass: Collapse all multiplications
        stack = []
        i = 0
        while i < len(toks):
            if toks[i] == '*':
                a = stack.pop()
                b = toks[i + 1]
                stack.append(a * b)
                i += 2
            else:
                stack.append(toks[i])
                i += 1
        # Now stack is a sequence of ints and '+' only
        true = 0
        i = 0
        while i < len(stack):
            if stack[i] == '+':
                i += 1
            else:
                true += stack[i]
                i += 1

        # Build all possible results by any parenthesization
        n = len(s)

        @lru_cache(None)
        def compute(lo: int, hi: int) -> set:
            # Base: single digit
            if lo == hi:
                return {int(s[lo])}

            res = set()
            # Try every operator position k between lo,hi
            for k in range(lo + 1, hi, 2):
                op = s[k]
                left_vals = compute(lo, k - 1)
                right_vals = compute(k + 1, hi)
                if op == '+':
                    for a in left_vals:
                        for b in right_vals:
                            v = a + b
                            if v <= 1000:
                                res.add(v)
                else:  # op == '*'
                    for a in left_vals:
                        for b in right_vals:
                            v = a * b
                            if v <= 1000:
                                res.add(v)
            return res

        all_vals = compute(0, n - 1)
        # The “incorrect but achievable” bucket:
        wrong = all_vals - {true}

        # Score the student answers
        score = 0
        for ans in answers:
            if ans == true:
                score += 5
            elif ans in wrong:
                score += 2
            # else +0
        return score
