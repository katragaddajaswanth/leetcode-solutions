class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        a = max(nums) 
        moves = 0

        for i in nums :
            moves += abs(i - a )

        return moves 