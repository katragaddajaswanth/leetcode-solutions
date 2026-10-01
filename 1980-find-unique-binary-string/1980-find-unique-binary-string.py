class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        
        b = []

        l = len(nums[0])

        for i in range(1<<l) :
            a = ""
            for j in range(l) :
                if i & (1<<j) :
                    a+="1"
                else :
                    a+="0"
            
            b.append(a)

        res = ""
        for i in b :
            if i not in nums :
                res = i

        return res