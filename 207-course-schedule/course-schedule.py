class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        preList = defaultdict(list)
        visited = set()

        for course, requirement in prerequisites:
            preList[course].append(requirement)

        def dfs(course):
            if course in visited:
                return False
            
            if not preList[course]:
                return True

            visited.add(course)

            for crs in preList[course]:
                if not dfs(crs):
                    return False

            visited.remove(course)
            preList[course] = []

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

                