class Solution:
    def clearDigits(self, s: str) -> str:

        a = []

        for i in s:
            if i.isdigit():
                if a:
                    a.pop()
            else:
                a.append(i)

        return "".join(a)

        