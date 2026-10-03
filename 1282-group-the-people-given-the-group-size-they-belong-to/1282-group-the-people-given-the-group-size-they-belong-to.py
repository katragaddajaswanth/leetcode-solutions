class Solution:
    def groupThePeople(self, g: list[int]) -> list[list[int]]:
        
        dictt = {}
        
        for i in range(len(g)) :

            if g[i] in dictt :
                dictt[g[i]].append(i)
            else :
                dictt[g[i]] = [i]

        res = []

        for size , listt in dictt.items() :

            for i in range(0,len(listt),size) :
                res.append(listt[i:i+size])

        return res

            

        