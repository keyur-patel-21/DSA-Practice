class Solution(object):
    def decodeString(self, s):
        curStr = ""
        curNum = 0

        strStack = []
        numStack = []

        for c in s:
            if c.isdigit():
                curNum = (curNum * 10) + int(c)     #solve this 

            elif c == "[":
                strStack.append(curStr)
                numStack.append(curNum)
                curStr = ""
                curNum = 0

            elif c == "]":
                count = numStack.pop()
                baby = curStr * count
                parent = strStack.pop()
                parent += baby
                curStr = parent


            else: 
                curStr += c
        
        return curStr