class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        preList = defaultdict(list)
        visited = set()

        for course, requirement in prerequisites:
            if course in preList:
                preList[course].append(requirement)
            else:
                preList[course] = [requirement]

        def dfs(course):
            if course in visited:
                return False
            
            if len(preList[course]) == 0:
                return True

            visited.add(course)

            for required_course in preList[course]:
                if not dfs(required_course): return False
            
            visited.remove(course)
            preList[course] = []

            return True

        for i in range(numCourses):
            if not dfs(i): return False
        return True

        