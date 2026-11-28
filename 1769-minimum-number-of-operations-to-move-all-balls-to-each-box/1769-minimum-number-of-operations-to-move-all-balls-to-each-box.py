class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        
        a = []

        for i in range(len(boxes)) :

            if boxes[i] == "1" :
                a.append(i)

        jamba_lakdi_jaaru_mitayaaaa = []
        for i in range(len(boxes)) :

            j = 0
            operation = 0
            while j < len(a) :

                operation += abs(i-a[j])
                j+=1
            jamba_lakdi_jaaru_mitayaaaa.append(operation)

        return jamba_lakdi_jaaru_mitayaaaa

