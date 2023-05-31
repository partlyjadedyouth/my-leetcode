class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = dict()
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        freq_keys = list(freq.keys())
        freq_vals = list(freq.values())
        return freq_keys[freq_vals.index(max(freq_vals))]
            