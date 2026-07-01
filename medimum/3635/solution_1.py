# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii

from typing import List

from bisect import bisect_right

def earliestFinishTime(landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
    INF = 10**30

    def build(starts: List[int], durations: List[int]):
        rides = sorted(zip(starts, durations))
        n = len(rides)

        sorted_starts = [s for s, _ in rides]

        prefix_min_duration = [INF] * n
        best = INF
        for i, (s, d) in enumerate(rides):
            best = min(best, d)
            prefix_min_duration[i] = best

        suffix_min_finish = [INF] * n
        best = INF
        for i in range(n - 1, -1, -1):
            s, d = rides[i]
            best = min(best, s + d)
            suffix_min_finish[i] = best

        return sorted_starts, prefix_min_duration, suffix_min_finish

    def best_after(first_starts, first_durations, second_starts, second_durations):
        starts2, pref_dur2, suff_finish2 = build(second_starts, second_durations)
        n2 = len(starts2)

        ans = INF

        for s, d in zip(first_starts, first_durations):
            end_time = s + d

            idx = bisect_right(starts2, end_time) - 1

            # Case 1: second ride already opened by end_time.
            if idx >= 0:
                ans = min(ans, end_time + pref_dur2[idx])

            # Case 2: second ride opens after end_time.
            nxt = idx + 1
            if nxt < n2:
                ans = min(ans, suff_finish2[nxt])

        return ans

    return min(
        best_after(landStartTime, landDuration, waterStartTime, waterDuration),
        best_after(waterStartTime, waterDuration, landStartTime, landDuration)
    )


landStartTime = [2,8]
landDuration = [4,1]
waterStartTime = [6]
waterDuration = [3]

print(earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration))