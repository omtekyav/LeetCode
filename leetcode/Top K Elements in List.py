from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count occurrences of each number
        count = {}  # Hashmap to store frequency of each element
        freq = [[] for i in range(len(nums) + 1)]  # List of buckets
        
        # Populate the count hashmap
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Populate the freq list with elements grouped by frequency
        for n, c in count.items():
            freq[c].append(n)
        
        # Collect the top k frequent elements
        res = []
        # Traverse the freq array from high to low (reverse order)
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
