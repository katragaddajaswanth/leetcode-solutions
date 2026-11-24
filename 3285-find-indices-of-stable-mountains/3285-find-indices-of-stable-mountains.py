class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        
        bobba_attu = []
        for i in range(1,len(height)) :
            if height[i-1] > threshold :
                bobba_attu.append(i)

        return bobba_attu