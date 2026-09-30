class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        
        count = 0
        digit = str(digit)

        for i in nums :
            i = str(i)
            count += i.count(digit)

        return count
