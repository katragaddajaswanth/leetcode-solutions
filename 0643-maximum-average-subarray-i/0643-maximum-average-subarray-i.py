class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        
        sume = sum(nums[:k])
        max_sum = sume

        for i in range(k,len(nums)) :
            sume += nums[i]
            sume -= nums[i-k]
            max_sum = max(sume, max_sum)

        return max_sum / k
        