from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Sort the list and remove duplicates
        nums = sorted(set(nums))  # Using set to remove duplicates
        print("Sorted and duplicate-free nums list:", nums)

        # Initialize counters for consecutive numbers
        count = 1  # Start with at least one number counted
        max_count = 1  # Track the maximum count of consecutive numbers

        # Check the difference between consecutive numbers
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                count += 1  # If the difference is 1, increment the counter
            else:
                # If the difference is not 1, update the max_count
                max_count = max(max_count, count)
                count = 1  # Reset the counter for a new consecutive group

        # After the loop, check the last group
        max_count = max(max_count, count)

        return max_count

