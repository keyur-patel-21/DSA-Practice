class Solution(object):
    def calculate(self, s):
        stack = []
        result = 0
        currNo = 0
        lastSign = "+"

        for i in range(len(s)):
            if s[i].isdigit():
                currNo = (currNo * 10) + (ord(s[i]) - ord("0"))
                print (currNo)
            if (((not s[i].isdigit()) and s[i] != " ") or (i == len(s)-1)):
                if lastSign == "+":
                    stack.append(currNo)
                if lastSign == "-":
                    stack.append(-currNo)                    
                if lastSign == "*":
                    stack.append(currNo * stack.pop())
                if lastSign == "/":
                    stack.append(int(stack.pop() / float(currNo)))

                currNo = 0
                lastSign = s[i]

        for digit in stack:
            result += digit

        return result

            

        