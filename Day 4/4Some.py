class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        new_s = []
        for i in range(len(nums)-3):
            for k in range(len(nums)-1,i,-1):
                left = i + 1
                right = k - 1
                while left<right:
                    if nums[right]+nums[k]+nums[i]+nums[left] == target and [nums[i],nums[left],nums[right],nums[k]] not in new_s:
                        new_s.append([nums[i],nums[left],nums[right],nums[k]])
                    if nums[right]+nums[k]+nums[i]+nums[left]<=target:
                        left += 1
                    else:
                        right -= 1
        return new_s
