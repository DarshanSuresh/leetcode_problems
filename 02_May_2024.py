class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen_negatives = set()
        max_k = -1
        
        for num in nums:
            if -num in seen_negatives:
                max_k = max(max_k, abs(num))
            else:
                seen_negatives.add(num)
        
        return max_k
