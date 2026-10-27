class Solution:
    def countEven(self, n: int) -> int:
        
        
        count = 0
        for i in range(1,n+1) :
            a = i
            sume = 0
            while a != 0 :
                digit = a % 10 
                sume = digit + sume 
                a = a//10

            if sume % 2 == 0 :
                count +=1

        return count
            