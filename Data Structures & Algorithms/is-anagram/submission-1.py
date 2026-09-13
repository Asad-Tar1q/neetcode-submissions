class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if lengths don't match, return false

        if len(s) != len(t):
            return False 

        #loop through s and add freq to dictionary
        
        s_dict = {}
        t_dict = {}
        for char in s:
            s_dict[char] = s_dict.get(char,0) + 1

        #check if we can find s in t
        for char in t:
            t_dict[char] = t_dict.get(char,0) + 1

        if s_dict == t_dict:
            return True
        return False
            
        print(s_dict)

        






        


        