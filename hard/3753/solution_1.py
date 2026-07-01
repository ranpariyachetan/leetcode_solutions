# https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii

from functools import lru_cache


def totalWaviness(num1: int, num2: int) -> int:

    def solve(num: int) -> int:
        """Sum of waviness for all integers in [0, num]."""
        if num < 0:
            return 0
        s = str(num)
        n = len(s)

        @lru_cache(maxsize=None)
        def dp(idx, tight, prev_digit, prev_dir, leading_zero):
            if idx == n:
                return (1, 0)

            limit = int(s[idx]) if tight else 9
            total_count = 0
            total_wav = 0

            for d in range(limit + 1):
                new_tight = tight and (d == limit)

                if leading_zero and d == 0:
                    cnt, wav = dp(idx + 1, new_tight, -1, 0, True)
                else:
                    is_change = False
                    if leading_zero:
                        new_prev, new_dir = d, 0
                    else:
                        new_prev = d
                        if d > prev_digit:
                            new_dir = 1
                            is_change = (prev_dir == 2)
                        elif d < prev_digit:
                            new_dir = 2
                            is_change = (prev_dir == 1)
                        else:
                            new_dir = 0

                    cnt, wav = dp(idx + 1, new_tight, new_prev, new_dir, False)
                    if is_change:
                        wav = wav + cnt

                total_count = total_count + cnt
                total_wav = total_wav + wav

            return (total_count, total_wav)

        _, result = dp(0, True, -1, 0, True)
        return result
        
    return solve(num2) - solve(num1 - 1)


num1 = 120
num2 = 130

print(totalWaviness(num1, num2))  # expected: 3

num1 = 8900
num2 = 9532

print(totalWaviness(num1, num2))