class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        
        maxy = 0 

        for account in accounts :
            
            maxy = max(maxy,sum(account))

        return maxy