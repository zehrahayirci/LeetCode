class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
    '''
    def majority-search (input-stream) :
        candidate , candidate-count = None, 0

        for it in input-stream:
            if candidate-count == 0:
                candidate , candidate_count = it, candidate_count +
            elif candidate == it:
                candidate_countt += 1
            else:
                candidate_count -= 1
            return candidate
    '''