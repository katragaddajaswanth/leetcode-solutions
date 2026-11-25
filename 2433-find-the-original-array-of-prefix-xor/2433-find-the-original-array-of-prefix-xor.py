class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        

        res = []
        res.append(pref[0])

        for i in range(1,len(pref)) :
            
            xor = pref[i]^pref[i-1]
            res.append(xor)

        return res
