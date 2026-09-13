from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        freq = defaultdict(int)
        max_list = []

        # for each number, we want the freq

        for num in nums:
            freq[num] +=1

        max_list = list(sorted(freq, key=freq.get, reverse = True))
        ans = max_list[:k]
        return ans
        

