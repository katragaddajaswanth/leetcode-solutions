class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        listt = []

        for i in range(1,n+1) :
            if n % i == 0 :
                listt.append(i)

        if len(listt) < k :
            return -1

        listt = sorted(listt)
        return listt[k-1]