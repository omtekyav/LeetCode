class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()  # Sort the list first
        for i in range(1, len(nums)):  # Start from the second element
            if nums[i] == nums[i - 1]:  # Compare current element with the previous one
                return True  # If they are equal, return True (duplicate found)
        return False  # If no duplicates were found, return False