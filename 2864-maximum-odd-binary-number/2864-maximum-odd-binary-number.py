class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        one = s.count("1")
        one -= 1
        b = len(s)
        res = ""
        for i in range(one) :
            res+="1"

        for i in range(b-one-1) :
            res+="0"

        res+="1"

        return res

