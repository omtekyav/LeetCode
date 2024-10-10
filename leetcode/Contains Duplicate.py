Duplicate Integer
Solved 
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
Example 2:

Input: nums = [1, 2, 3, 4]

Output: falseclass Solution1:
    def hasDuplicate(self, nums: List[int]) -> bool:

        num_set = set()

        for i in nums:
            if i in num_set:
                return True
            num_set.add(i)
        return False
