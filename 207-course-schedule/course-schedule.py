class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        
        indArray = [0] * numCourses
        adjList = {}

        for pre in prerequisites:
            indArray[pre[0]] += 1
            if pre[1] in adjList:
                adjList[pre[1]].append(pre[0])
            else:
                adjList[pre[1]] = [pre[0]]

        q = collections.deque() 
        count = 0

        for i in range(len(indArray)):
            if indArray[i] == 0:
                q.append(i)
                count += 1
        
        if count == numCourses:
            return True
        if not q:
            return False

        while q:
            cur = q.popleft()
            if cur in adjList:
                dependents = adjList[cur]
                for dep in dependents:
                    indArray[dep] -= 1
                    if indArray[dep] == 0:
                        q.append(dep)
                        count += 1
                        if count == numCourses:
                            return True
        
        return False