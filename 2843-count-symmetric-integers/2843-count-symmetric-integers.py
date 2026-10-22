class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:

        count = 0

        for i in range(low, high + 1):
            a = str(i)
            b = len(a)

            if b % 2 != 0:
                continue

            first = sum(int(x) for x in a[:b//2])
            second = sum(int(x) for x in a[b//2:])

            if first == second:
                count += 1

        return count