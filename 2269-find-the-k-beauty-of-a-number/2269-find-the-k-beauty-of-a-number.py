class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        original = num
        count = 0

        num = str(num)
        for i in range(len(num)-k+1)  :
            a = num[i:i+k]
            b = int(a)

            if b == 0 :
                continue

            if original % b == 0 :
                count +=1

        
        return count
