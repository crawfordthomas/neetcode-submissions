class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j, max = 0, len(heights) - 1, 0

        while i < j:
            area = min(heights[i], heights[j]) * abs(i - j)
            print(area)
            if area > max:
                max = area
            if heights[i] > heights[j]:
                j -= 1
            else: 
                i += 1
            
        
        return max