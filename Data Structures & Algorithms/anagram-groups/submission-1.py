class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # check for anagram 
        sortedList = []

        sorted_dict = defaultdict(list)

        for word in strs:
            sortedList.append("".join(sorted(word)))

        i = 0
        for sortedWord in sortedList:
            sorted_dict[sortedWord].append(strs[i])
            i+=1
        
        return list(sorted_dict.values())


        