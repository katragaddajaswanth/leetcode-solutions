class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        res = []
        for i in range(1,len(A)+1) :
            a = A[:i]
            b = B[:i]

            a = sorted(a)
            b = sorted(b) 
            count = 0

            for j in range(len(a)) :
                if a[j] in b  :
                    count+=1

            res.append(count)


        return res

            