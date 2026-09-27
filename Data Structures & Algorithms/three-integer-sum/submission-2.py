class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
      
        results = []


        for m in range(len(nums)):
            l = m + 1
            r = len(nums) - 1 
            print("M:" , m)

            if l == m or m == r:
                continue
            if m > 0 and nums[m] == nums[m - 1]:
                continue
            while r > l:
               

                if (nums[l] + nums[m] + nums[r]) > 0:
                    r-=1

                elif (nums[l] + nums[m] + nums[r]) < 0:
                    l+=1
                
                elif (nums[l] + nums[m] + nums[r]) == 0:
                    results.append([nums[l],nums[m],nums[r]])
                    l+=1
                    r-=1

                    while r > l and nums[l] == nums[l - 1]:
                        l += 1

        return results
            


        