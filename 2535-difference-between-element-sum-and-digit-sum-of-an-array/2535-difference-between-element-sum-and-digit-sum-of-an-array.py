class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        
        sume = 0
        sumee = 0
        for i in nums :
            sume += i

        for j in nums :
            while j != 0 :
                digit = j % 10 
                sumee = digit + sumee
                j = j//10

        return abs(sume - sumee) 