class Solution:
    def sumBase(self, n: int, k: int) -> int:
        
        rev_baseK = 0
        sume = 0
        while n :
            digit = n % k
            rev_baseK += digit*10
            sume+=digit
            n//=k

        return sume
        