from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1dict = defaultdict(int)
        windowDict = defaultdict(int)
        for item in s1:
            s1dict[item] +=1
        
        print(s1dict)

        l = 0
        for right in range(len(s2)):
            window = right - l + 1
            print(windowDict)
            windowDict[s2[right]] += 1

            if len(s1) < window:
                print(s2[l])
                windowDict[s2[l]] -= 1
                if windowDict[s2[l]] == 0:
                    del windowDict[s2[l]]
                l+=1 
                window = right - l + 1
                

            
            if s1dict == windowDict:
                return True  
        
        return False

        


