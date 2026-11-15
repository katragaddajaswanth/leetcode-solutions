class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        
        a = []
        for i in matrix :
            c = i.count(1)
            a.append(c)

        return a