class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = {}
        new_list = []
        for i in range(len(nums)):
            val = target - nums[i]
            if val in new_nums:
                new_list.append(new_nums.get(val))
                new_list.append(i)
            new_nums[nums[i]] = i
        return new_list
        