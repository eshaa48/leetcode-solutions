class Solution(object):
    def sortArray(self, nums):
        # base case: agar list ki length 0 ya 1 ho to woh already sorted hai
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        # recursively left aur right halves ko sort karo
        left_sort = self.sortArray(nums[:mid])
        right_sort = self.sortArray(nums[mid:])
        # dono sorted halves ko merge karke result return karo
        return self.merge(left_sort, right_sort)

    def merge(self, left_sort, right_sort):
        i, j = 0, 0
        result = []
        # dono arrays ke elements compare karke chhota wala result me daalo
        while i < len(left_sort) and j < len(right_sort):
            if left_sort[i] <= right_sort[j]:
                result.append(left_sort[i])
                i += 1
            else:
                result.append(right_sort[j])
                j += 1
        # agar left me kuch bacha ho to unko add karo
        if i < len(left_sort):
            result.extend(left_sort[i:])
        # agar right me kuch bacha ho to unko add karo
        if j < len(right_sort):
            result.extend(right_sort[j:])
        return result
