# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i

from typing import List

def earliestFinishTime(landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
    m = len(landStartTime)
    n = len(waterStartTime)

    answer = float("inf")

    land_finish , water_finish = float("inf"), float("inf")

    for i in range(m):
        land_finish = min(land_finish, landStartTime[i] + landDuration[i])

    for j in range(n):
        water_finish = min(water_finish, max(land_finish, waterStartTime[j]) + waterDuration[j])

    answer = min(answer, water_finish)

    land_finish , water_finish = float("inf"), float("inf")

    for j in range(n):
        water_finish = min(water_finish, waterStartTime[j] + waterDuration[j])

    for i in range(m):
        land_finish = min(land_finish, max(water_finish, landStartTime[i]) + landDuration[i])

    answer = min(answer, land_finish)

    return answer


landStartTime = [2,8]
landDuration = [4,1]
waterStartTime = [6]
waterDuration = [3]

print(earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration))

landStartTime = [5]
landDuration = [3]
waterStartTime = [1]
waterDuration = [10]

print(earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration))

landStartTime = [99]
landDuration = [59]
waterStartTime = [99, 54]
waterDuration = [85, 20]

print(earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration))