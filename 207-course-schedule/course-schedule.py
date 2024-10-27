class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        Visitset = set()

        def dfs(crs):
            if crs in Visitset:
                return False
            if preMap[crs] == []:
                return True
            
            Visitset.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre): return False
            
            Visitset.remove(crs)
            preMap[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i): return False
        return True

        