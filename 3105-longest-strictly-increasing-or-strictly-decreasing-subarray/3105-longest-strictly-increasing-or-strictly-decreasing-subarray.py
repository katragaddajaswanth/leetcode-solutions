class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        a = []
        for i in range(len(nums)):
            b = []
            for j in range(i+1,len(nums)+1) :
                b = nums[i:j]
                a.append(b)


        maxy = 1

        for i in a :
            inc = all(i[k] < i[k+1] for k in range(len(i)-1))
            dec = all(i[k] > i[k+1] for k in range(len(i)-1))

            if (inc or dec) and len(i) > maxy :
                maxy = len(i)


        return maxy