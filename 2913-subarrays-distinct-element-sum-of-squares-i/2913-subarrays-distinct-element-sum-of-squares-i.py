class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        
        sub = []
        for i in range(len(nums)) :
            for j in range(i+1,len(nums)+1) :
                sub.append(nums[i:j])

        sume = 0
        for i in sub :
            i = set(i)
            a = len(i)
            sume += a**2
       
        return sume