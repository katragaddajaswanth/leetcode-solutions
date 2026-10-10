
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:

        k = len(p)
        res = []

        if k > len(s):
            return res

        freq_s = [0] * 26
        freq_p = [0] * 26

        for i in range(k):
            freq_s[ord(s[i]) - ord('a')] += 1
            freq_p[ord(p[i]) - ord('a')] += 1

        if freq_s == freq_p:
            res.append(0)

        for i in range(k, len(s)):
            freq_s[ord(s[i]) - ord('a')] += 1
            freq_s[ord(s[i-k]) - ord('a')] -= 1

            if freq_s == freq_p:
                res.append(i-k+1)

        return res
