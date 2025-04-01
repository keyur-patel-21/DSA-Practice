class Solution(object):
    def addOperators(self, num, target):
        result = []

        def helper(pivot, calc, tail, path):
            # base
            
            if pivot == len(num):
                if calc == target:
                    result.append(path)
                return


            #logic
            for i in range(pivot, len(num)):

                if num[pivot] == "0" and pivot != i:
                    continue 

                currNumStr = num[pivot:i+1]
                currNum = int(currNumStr)

                if pivot == 0:
                    helper(i+1, currNum, currNum, path + currNumStr)
                else:
                    # +
                    helper(i+1, calc+currNum, currNum, path + "+" +currNumStr)

                    # -
                    helper(i+1, calc-currNum, -currNum, path + "-" + currNumStr)

                    # * 
                    helper(i+1, (calc-tail)+(tail*currNum), tail*currNum, path + "*" + currNumStr)

        helper(0, 0, 0, "")
        return result
        