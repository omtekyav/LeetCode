from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n  # Initialize the result list with 1s
        
        # Calculate the left products
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        
        # Calculate the right products and update the result
        right_product = 1
        for i in range(n-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result

# Example usage
solution = Solution()
arr = [2, 3, 5, 7]
result = solution.productExceptSelf(arr)

# Print the results
print("Product Except Self List:", result)
