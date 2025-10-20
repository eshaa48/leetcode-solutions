class Solution(object):
    def twoSum(self, nums, target):
        # Step 1: create an empty hash map
        hashmap = {}
        
        # Step 2: iterate through the list
        for i, num in enumerate(nums):
            # find the complement (what number we need to reach target)
            complement = target - num
            
            # Step 3: check if complement already exists in hashmap
            if complement in hashmap:
                # if yes, return their indices
                return [hashmap[complement], i]
            
            # Step 4: otherwise store the number with its index
            hashmap[num] = i

        