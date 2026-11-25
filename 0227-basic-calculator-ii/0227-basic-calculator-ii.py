class Solution:
    def calculate(self, s: str) -> int:
        
        a = []
        op = "+"
        num = 0

        for i in range(len(s)) :
            
            if s[i].isdigit() :
                num = num*10 + int(s[i])

            if s[i] in "+-/*" or i == len(s)-1 :

                if op == "+" :
                    a.append(num)
                elif op == "-" :
                    a.append(-num)
                elif op == "*" :
                    a.append(a.pop() * num)
                elif op == "/" :
                    x = a.pop()
                    a.append(abs(x)// num * (1 if x >= 0 else -1))

                op = s[i] if s[i] in "+-*/" else ""
                num = 0

        return sum(a)