class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        a = s.split()
        count = 0
        res = ""
        
        for i in a :
            res+=i
    
            count+=1
            if count >= k :
                break
            else :
                res+=" "


        return res