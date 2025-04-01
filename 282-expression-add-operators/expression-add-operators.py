class Solution(object):
    def addOperators(self, num, target):
        result = []

        def helper(pivot, calc, tail, path):
            # base
            if pivot == len(num):
                if calc == target:
                    result.append(path)

            # logic
            for i in range(pivot, len(num)):
                if num[pivot] == "0" and pivot != i:        #edge case. EX: 105
                    return
                    
                currNum = int(num[pivot:i+1])

                if pivot == 0:
                    helper(i+1, currNum, currNum, path + str(currNum))
                else:
                    # +
                    helper(i+1, calc + currNum, currNum, path + "+" + str(currNum))

                    # -
                    helper(i+1, calc - currNum, -currNum, path + "-" + str(currNum))

                    # *
                    helper(i+1, (calc-tail) + (currNum*tail), currNum*tail, path + "*" + str(currNum))
        helper(0, 0, 0, "")
        return result
        