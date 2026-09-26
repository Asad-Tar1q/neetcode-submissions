from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqSlidingWindow = defaultdict(int)
        l = 0
        longest = 0
        
        for right in range(len(s)):
            freqSlidingWindow[s[right]] +=1
            window = right - l + 1
            maxValue = max(freqSlidingWindow.values())
            while (window - maxValue ) > k:
                freqSlidingWindow[s[l]] -= 1
                l+=1
                window = right - l + 1


            longest = max(window, longest)
        
        return longest


            
            

        print(freq)
        # Find longest in row, turn everything after it 
        



        