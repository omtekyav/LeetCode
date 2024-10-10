Two Integer Sum
Solved 
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
Constraints:

2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000



Solution:
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # Create a dictionary to store numbers and their indices
        
        for i, num in enumerate(nums):  # Iterate through the list with indices
            complement = target - num  # Calculate the complement needed for the target
            
            if complement in num_map:  # Check if the complement exists in the map
                return [num_map[complement], i]  # Return the indices of the two numbers
            
            num_map[num] = i  # Add the current number and its index to the map
            
        return []  # This line won't be reached as per problem constraints

