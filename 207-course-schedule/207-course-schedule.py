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
        cycle = set()
        courses_map   = {course:[] for course in range(numCourses)} # {0:[], 1:[], 2:[], 3:[], 4:[]}
        # Mapping each course to : prereq list (creating the graph)
        for course in prerequisites: # prerequisite = 
            courses_map[course[0]].append(course[1])
        
        def dfs(course):
            if course in cycle: return False # if it is visited twice, so there is a cycle
            if course in hasVisited: return True # if there is no required cources to finish
            
            cycle.add(course)
            for neighbor in courses_map[course]:
                if not dfs(neighbor): # not dfs(neighbor) == dfs(neighbor) == False
                    return False
            # remove if, cuz we're no longer visiting this node(we have already finish visiting this node)
            cycle.remove(course)
            hasVisited.add(course)
            # Make it empty in case we need to check that this graph has cycle or not, 
            # without running the same functionallity, we imidiately return True
            return True
        # We should run this loop in case the graph is not fully connected
        for course in courses_map:
            if not dfs(course):
                return False
            
        return True