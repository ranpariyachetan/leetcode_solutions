# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i

def totalWaviness(num1: int, num2: int) -> int:
    answer = 0
    if num1 < 100 and num2 < 100:
        return answer
    
    if num1 < 100:
        num1 = 100

    for num in range(num1, num2 + 1):
        while num > 100:
            d1 = num % 10
            d2 = (num // 10) % 10
            d3 = (num // 100) % 10

            answer += (d2 > max(d1, d3) or d2 < min(d1, d3))

            num = num // 10

    return answer


num1 = 120
num2 = 130
print(totalWaviness(num1, num2))

num1 = 198
num2 = 202
print(totalWaviness(num1, num2))

num1 = 4848
num2 = 4848
print(totalWaviness(num1, num2))