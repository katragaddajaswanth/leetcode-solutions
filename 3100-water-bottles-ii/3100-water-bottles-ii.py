class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        
        original = numBottles

        while numExchange <= numBottles :
            numBottles-=numExchange
            numExchange+=1
            original +=1
            numBottles+=1

        return original
