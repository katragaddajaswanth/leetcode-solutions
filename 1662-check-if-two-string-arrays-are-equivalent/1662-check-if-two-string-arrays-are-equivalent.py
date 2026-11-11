class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        
        res1 = ""
        res2 = ""

        for i in word1 :
            res1+=i

        for j in word2 :
            res2+=j

        print(res1)
        print(res2)

        if res1 == res2 :
            return True
        else :
            return False

        