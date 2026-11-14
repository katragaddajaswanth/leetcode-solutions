class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        
        subsets = []
        for i in range(len(nums)) :
            for j in range(i+1,len(nums)+1) :
                subsets.append(nums[i:j])

        mini = float("inf")

        for i in subsets :
            
            if l <= len(i) <= r and sum(i) > 0 :
                mini = min(mini,sum(i))
                
            

        return mini if mini != float("inf") else -1
