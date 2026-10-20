class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        
        rev = []

        for i in nums :
            a = str(i)
            a = a[::-1]
            a = int(a)
            rev.append(a)

        for i in rev :
            nums.append(i)

        return len(set(nums))