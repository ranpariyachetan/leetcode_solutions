# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i

def numberOfStableArrays(zero: int, one: int, limit: int) -> int:
    MOD = 1_000_000_007
    def modinv(n) -> int:
        x, y, px, py = 0, 1, 1, 0

        m = MOD
        while m != 0:
            q = n // m
            n, m = m, n%m
            px, x = x, px-q*x
            py, y = y, py-q*y

        return px
    
    def ncr(n , r) -> int:
        if r > n//2:
            r = n - r

        num, den = 1, 1

        for i in range(1, r + 1):
            num = (num * (n - i + 1)) % MOD
            den = (den * i) % MOD

        return (num * modinv(den)) % MOD

    def splitways(n, k, limit) -> int:
        if n == k:
            return 1
        if n > k * limit:
            return 0
        total, flag, remaining = 0, 1, n

        j = 0

        while (j<=k and k <= remaining):
            term = ncr(k, j) * ncr(remaining - 1, k - 1)
            total = (total + flag * term + MOD * MOD) % MOD
            flag = -flag
            remaining -= limit
            j +=1
        return total

    prev, curr, next = 0, splitways(one, 1, limit), splitways(one, 2, limit)

    result = 0
    for k in range(1, zero + 1):
        choices = (prev + 2 * curr + next) * splitways(zero, k, limit)
        result = (result + choices) % MOD
        prev, curr, next = curr, next, splitways(one, k+2, limit)
    return result


zero = 13
one = 20
limit = 93

expected = 573166440

print(numberOfStableArrays(zero, one, limit))