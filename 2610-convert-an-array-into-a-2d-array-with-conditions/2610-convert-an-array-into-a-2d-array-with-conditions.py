class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        
        counts = []
        for i in nums :
            if nums.count(i) not in counts :
                counts.append(nums.count(i))


        i = 0 
        result = []

        while i < max(counts) :
            res = []
            for j in nums:
                if nums.count(j) > i and j not in res :
                    res.append(j)
            i+=1
            result.append(res)

        return result

