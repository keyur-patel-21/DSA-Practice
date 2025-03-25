"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        empDet = {}
        result = 0

        for emp in employees:
            empDet[emp.id] = [emp.importance, emp.subordinates]

        if id not in empDet:
            return 0

        q = collections.deque()
        q.append(id)

        while q:
            for i in range(len(q)):
                curId = q.popleft()
                curemp = empDet[curId]
                result += curemp[0]
                if curemp[1] is not None:
                    for sub in curemp[1]:
                        q.append(sub)

        return result
