class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        output = []
        cycle  = set()
        hasVisited  = set()
        
        courses_map = {course_number: [] for course_number in range(numCourses)}
        
        for course, prerequisite in prerequisites:
            courses_map[course].append(prerequisite)
            
        def dfs(course):
            if course in cycle:
                return False
            if course in hasVisited:
                return True
            
            cycle.add(course)
            for neighbor in courses_map[course]:
                if not dfs(neighbor):
                    return False
            cycle.remove(course)
            hasVisited.add(course)
            output.append(course)
            return True
              
        for course in courses_map:
            if not dfs(course):
                return []
        return output