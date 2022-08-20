class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        # Test Case:
        #   [[0,1], [0,2], [1,3], [1,4], [3,4]] , numCourses = 5
        #   courses_map = {0:[1,2], 1:[3,4], 2:[], 3:[4], 4:[]}
        #   hasVisited = {0, 1, 3, 4}
        
        # Time Complexity : O(V+E)
        # Space Complexity: O(V+E)
        # Where E is the number of edges and V is the number of vertices
        
        hasVisited = set()
        courses_map   = {i:[] for i in range(numCourses)} # {0:[], 1:[], 2:[], 3:[], 4:[]}
        # Mapping each course to : prereq list (creating the graph)
        for course in prerequisites: # prerequisite = 
            courses_map[course[0]].append(course[1])
        
        def dfs(course):
            if course in hasVisited: return False
            if courses_map[course] == []:
                return True
            
            hasVisited.add(course)
            for neighbor in courses_map[course]:
                if not dfs(neighbor): # not dfs(neighbor) == dfs(neighbor) == False
                    return False
            hasVisited.remove(course)
            # Make it empty in case we need to check that this graph has cycle or not, 
            # without running the same functionallity, we imidiately return True
            courses_map[course] = [] 
            return True
        # We should run this loop in case the graph is not fully connected
        for course in courses_map:
            if not dfs(course):
                return False
            
        return True