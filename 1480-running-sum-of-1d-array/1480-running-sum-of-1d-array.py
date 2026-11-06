class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        
        running_sum = []
        sume = 0
        for i in nums :
            sume += i
            running_sum.append(sume)

        return running_sum