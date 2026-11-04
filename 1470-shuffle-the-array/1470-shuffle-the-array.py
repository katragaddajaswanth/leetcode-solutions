class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        a = len(nums)//2
        res = []

        for i in range(len(nums)//2) : 
            res.append(nums[i])
            res.append(nums[a+i])

        return res