class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = 0
        highestArea = 0

        while r > l:
            area = min(heights[l],heights[r]) * (r-l)
            if area > highestArea:
                highestArea = area
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
            

        return highestArea



        