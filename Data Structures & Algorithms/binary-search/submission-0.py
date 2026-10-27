class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        
        while hi >= lo:
            mid = (hi + lo) // 2
            print("Mid", mid)
            value = nums[mid]
            print("Value", value)

            if value == target:
                return mid 
            
            elif value < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1 


        