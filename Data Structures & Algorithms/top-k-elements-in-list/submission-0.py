class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for n in nums:
            if freqs.get(n) != None:
                freqs[n] += 1
            else:
                freqs[n] = 1
        items = sorted(freqs,key = lambda item: freqs[item], reverse=True)
        return items[:k]

        