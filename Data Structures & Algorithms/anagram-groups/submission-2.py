from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #sort all the words 
        #make the sorted word my key and all the words that correspond to each sorted word the values
        
        keys = []

        dic = defaultdict(list)

        for i in range(len(strs)):
            keys.append("".join(sorted(strs[i])))
        
        j = 0
        for key in keys:
            dic[key].append(strs[j])
            j+=1

        return list(dic.values())




        


        