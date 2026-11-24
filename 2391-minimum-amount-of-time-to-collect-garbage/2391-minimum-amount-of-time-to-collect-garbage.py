
class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        
        traveled = 0

        lastG = max(i for i in range(len(garbage)) if "G" in garbage[i]) if any("G" in x for x in garbage) else -1
        lastP = max(i for i in range(len(garbage)) if "P" in garbage[i]) if any("P" in x for x in garbage) else -1
        lastM = max(i for i in range(len(garbage)) if "M" in garbage[i]) if any("M" in x for x in garbage) else -1

        for i in range(lastG + 1):
            traveled += garbage[i].count("G")
            if i < lastG:
                traveled += travel[i]

        for i in range(lastP + 1):
            traveled += garbage[i].count("P")
            if i < lastP:
                traveled += travel[i]

        for i in range(lastM + 1):
            traveled += garbage[i].count("M")
            if i < lastM:
                traveled += travel[i]

        return traveled
