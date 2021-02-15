import numpy as np
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        print(len(mat))
        n = np.array(mat)
        sums= n.sum(axis=1) + np.arange(n.shape[0])*1e-6
        return list(np.argsort(sums)[0:k])