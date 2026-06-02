# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i

from typing import List

def earliestFinishTime(landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
    m = len(landStartTime)
    n = len(waterStartTime)

    answer = float("inf")

    for i in range(m):
        for j in range(n):
            land = landStartTime[i] + landDuration[i]
            land_water = max(land, waterStartTime[j]) + waterDuration[j]
            answer = min(answer, land_water)

            water = waterStartTime[j] + waterDuration[j]
            water_land = max(water, landStartTime[i]) + landDuration[i]
            answer = min(answer, water_land)

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