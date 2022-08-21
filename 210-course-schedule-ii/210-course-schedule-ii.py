class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        # First Approach
        output = []
        queue = deque()
        courses_map = {course_number: [] for course_number in range(numCourses)}
        inDegree = [0]*numCourses
        
        for course, prerequisite in prerequisites:
            courses_map[prerequisite].append(course)
            inDegree[course] += 1
        
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        
        while queue:
            current_node = queue.popleft()
            for neighbor in courses_map[current_node]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
            output.append(current_node)
        return output if len(output)==numCourses else []
        
        
        # Another approach
        """
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
            # Add the course to the current visiting path
            cycle.add(course)
            for neighbor in courses_map[course]:
                if not dfs(neighbor):
                    return False
            # Remove the course from the current visiting path
            cycle.remove(course)
            # Add the course to the have visited list
            hasVisited.add(course)
            output.append(course)
            return True
              
        for course in courses_map:
            if not dfs(course):
                return []
        return output
        """