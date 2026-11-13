class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        
        res = [""]*(len(indices)+1)

        for i in range(len(s)) :

            res[indices[i]] = s[i]


        ans = ""
        for  i in res :
            ans+=i

        return ans