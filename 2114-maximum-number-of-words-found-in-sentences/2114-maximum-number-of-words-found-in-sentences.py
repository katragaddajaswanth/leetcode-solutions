
class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        
        maxy = 0

        for a in sentences:
            b = a.count(" ")
            maxy = max(b + 1, maxy)

        return maxy
