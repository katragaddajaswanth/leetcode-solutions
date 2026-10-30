class Solution:
    def minMaxDifference(self, n: int) -> int:
        # Digits, most significant first
        digits = []
        temp = n
        while temp:
            digits.append(temp % 10)
            temp //= 10
        digits.reverse()

        # Maximum: replace the FIRST non-9 digit (and all its copies) with 9
        maxy = -1
        for d in digits:
            if d != 9:
                maxy = d
                break

        ans = 0
        for d in digits:
            ans = ans * 10 + (9 if d == maxy else d)
        maximum = ans

        # Minimum: replace the first digit (and all its copies) with 0
        miny = digits[0]
        ans = 0
        for d in digits:
            ans = ans * 10 + (0 if d == miny else d)
        minimum = ans

        return maximum - minimum