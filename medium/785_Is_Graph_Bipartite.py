class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = {}
        def check_dfs(pos):
            for nn in graph[pos]:
                if nn in color:
                    if color[nn] == color[pos]:
                        return False
                else:
                    color[nn] = 1 - color[pos]
                    if not check_dfs(nn):
                        return False
            return True
            
        
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0 
                if not check_dfs(i):
                    return False
        return True