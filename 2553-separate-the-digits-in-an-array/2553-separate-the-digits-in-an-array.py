class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        
        res = []
        for i in nums :
            a = str(i)
            for j in a :
               res.append(int(j))

        return res
