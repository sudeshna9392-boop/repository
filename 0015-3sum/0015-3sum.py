class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()  # Sort to use two-pointer technique and avoid duplicates
        
        for i in range(len(nums) - 2):
            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Move left and right pointers, skipping duplicates
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif total < 0:
                    left += 1  # Need a larger sum
                else:
                    right -= 1  # Need a smaller sum
        
        return res


# Example usage
nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))
        