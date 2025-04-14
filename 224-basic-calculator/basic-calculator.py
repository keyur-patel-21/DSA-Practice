class Solution(object):
    def calculate(self, s):
        stack = []
        currNo = 0
        lastSign = "+"
        res = 0
        s = s.strip()

        for i, ch in enumerate(s):
            if ch.isdigit():
                currNo = (currNo * 10) + (ord(ch) - ord("0"))
            
            if ch == "(":
                if lastSign == "-":
                    stack.append(-1)
                else:
                    stack.append(1)
                stack.append(ch)
                currNo = 0
                lastSign = "+"
            if (ch == "+" or ch == "-"):
                if lastSign == "-":
                    stack.append(-currNo)
                else:
                    stack.append(currNo)
                currNo = 0
                lastSign = ch
            if ch == ")":   
                if lastSign == "-":
                    stack.append(-currNo)
                else:
                    stack.append(currNo)
                temp_res = 0
                while stack[-1] != "(":
                    temp_res += stack.pop()
                stack.pop()
                stack.append(temp_res * stack.pop())
                currNo = 0
                lastSign = "+"

        if lastSign == "-":
            stack.append(-currNo)
        else:
            stack.append(currNo)

        for digit in stack:
            res += digit

        return res

        
                     