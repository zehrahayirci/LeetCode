class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index = {}
        citations.sort()
        sol = len(citations)
        for paper in citations:
            h_index[paper] = sum( citations[x] >= paper for x in range(len(citations)))
            #print(h_index)
            if h_index[paper] >= paper:
                sol = paper
            else:
                sol =max(sol,min( h_index[i] for i in h_index.keys()))
        return sol