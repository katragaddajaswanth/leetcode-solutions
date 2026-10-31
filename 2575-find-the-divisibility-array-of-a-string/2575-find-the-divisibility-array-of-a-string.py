class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        
        res = []
        num = 0

        for i in range(0,len(word)) :
            
            a = word[i]
            a = int(a)

            num = (num*10 + a) % m 

            if num == 0 :
                res.append(1)
            else :
                res.append(0)

        return res