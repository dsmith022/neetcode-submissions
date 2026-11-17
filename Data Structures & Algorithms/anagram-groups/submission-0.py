class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        masterFreqs = []
        letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        for s in strs:
            freqs = {}
            for char in s:
                if char in freqs:
                    freqs[char] += 1
                else: 
                    freqs[char] = 1
            if freqs in masterFreqs:
                idx = masterFreqs.index(freqs)
                ans[idx].append(s)
            else:
                ans.append([s])
                masterFreqs.append(freqs)
        return ans

             