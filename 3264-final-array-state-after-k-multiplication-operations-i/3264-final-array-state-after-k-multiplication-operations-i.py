from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        for _ in range(k):
            mini = min(nums)

            for j in range(len(nums)):
                if nums[j] == mini:
                    nums[j] = nums[j] * multiplier
                    break

        return nums