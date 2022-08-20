class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        # [[0,1], [0,2], [1,3], [1,4], [3,4]] , numCourses = 5
        stack = []
        hasVisited = set()
        hash_map = {i:[] for i in range(numCourses)} # {0:[], 1:[], 2:[], 3:[], 4:[]}
        
        for course in prerequisites: # prerequisite = 
            hash_map[course[0]].append(course[1])
        # hash_map = {0:[1,2], 1:[3,4], 2:[], 3:[4], 4:[]}
        
        
        
        # hasVisited = {0, 1, 3, 4}
        # stack = [4,3]
        def dfs(key):
            if key in hasVisited: return False
            if hash_map[key] == []:
                # hasVisited.add(key)
                return True
            
            hasVisited.add(key)
            for neighbor in hash_map[key]:
                if dfs(neighbor) == False:
                    return False
            hasVisited.remove(key)
            hash_map[key] = []
            #stack.append(key)
            return True
            
        for key in hash_map:
            # if key not in hasVisited:
                # result = dfs(key)
                
            if not dfs(key):
                return False
            
        return True